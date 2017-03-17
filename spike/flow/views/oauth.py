import logging
import os

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.http import Http404
from django.shortcuts import redirect
from dropbox.oauth import *

from ..models import DropboxToken

logger = logging.getLogger(__name__)

# Create your views here.
APP_KEY = os.environ['DBX_APP_KEY']
APP_SECRET = os.environ['DBX_APP_SECRET']

def get_dropbox_auth_flow(session):
    redirect_uri = "https://localhost:8000/dropbox-auth-finish"
    return DropboxOAuth2Flow(
        APP_KEY, APP_SECRET, redirect_uri, session,
        "dropbox-auth-csrf-token")

# URL handler for /dropbox-auth-start
def dropbox_auth_start(request):
    authorize_url = get_dropbox_auth_flow(request.session).start()
    return redirect(authorize_url)


def dropbox_auth_finish(request):
    try:

        flow = get_dropbox_auth_flow(request.session)
        oauth_result = flow.finish(request.GET)

    except BadRequestException as e:
        raise Http404
    except BadStateException as e:
        # Start the auth flow again.
        redirect("/dropbox-auth-start")
    except CsrfException as e:
        raise Http404
    except NotApprovedException as e:
        print('Not approved?  Why not?')
        return redirect("/home")
    except ProviderException as e:
        logger.log("Auth error: %s" % (e,))
        raise Http404

    else:
        request.session['dbx_oauth'] = {'access_token':oauth_result.access_token,
                                        'user_id': oauth_result.user_id}


        user = authenticate(dbx_user_id=oauth_result.user_id)
        login(request, user)

        try: #save token for later
            d = DropboxToken.objects.get(user=user)
            d.access_token = oauth_result.access_token
            d.save()
        except DropboxToken.DoesNotExist:
            DropboxToken.objects.create(user=user, access_token=oauth_result.access_token)


        return redirect('home')


def logout(request):
    auth_logout(request)
    return redirect('home')

