from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render
from dropbox import dropbox


@login_required
def story_list(request):
    context = {}
    app_key = request.user.dbx.access_token
    dbx = dropbox.Dropbox(app_key)

    all_boards = []
    for board in dbx.files_list_folder('/stories/').entries:
        scenes = {}
        submissions = {}
        # import ipdb; ipdb.sset_trace();
        # /story/ad2/scenes/<scene{number}>/(preview|<scene{number}>)
        for scene in dbx.files_list_folder(board.path_lower+'/scenes').entries:
            scene_key = scene.path_lower.split('/')[-1]
            scenes[scene_key] = {'preview_link': get_preview_link(dbx, scene.path_lower),
                                 'scene_frames': []}
            for scene_image in dbx.files_list_folder(scene.path_lower).entries:
                scene_frame_link = dbx.files_get_temporary_link(scene_image.path_lower).link
                scenes[scene_key]['scene_frames'].append(scene_frame_link)

        # /story/ad2/submissions/<submission_name>/<scene{number}>/(preview|render)
        for scene_submission in dbx.files_list_folder(board.path_lower+'/submissions').entries:
            submission_key = scene_submission.path_lower
            # for scene_submission in dbx.files_list_folder(submission.path_lower).entries:
            submissions[submission_key] = {
               'preview_link': get_preview_link(dbx, scene_submission.path_lower),
               'render_frames': []}
            for render_image in dbx.files_list_folder(scene_submission.path_lower+'/renders').entries[::1]:
                render_frame_link = dbx.files_get_temporary_link(render_image.path_lower).link
                submissions[submission_key]['render_frames'].append(render_frame_link)

        board_info = {'name': board.name,
                      'scenes': scenes,
                      'submissions': submissions}
        all_boards.append(board_info)

    context['all_boards'] =  all_boards
    return render(request, 'flow/story_list.html', context=context)


def get_preview_link(dbx, path):
    try:
        return dbx.files_get_temporary_link(path + '/preview.jpg').link
    except Exception:
        pass
    try:
        return dbx.files_get_temporary_link(path + '/preview.png').link
    except Exception:
        return ""

@login_required
def story_detail(request, slug):
    app_key = request.user.dbx.access_token
    dbx = dropbox.Dropbox(app_key)

    context = []
    for scene in dbx.files_list_folder('/stories/'+slug).entries:
        img = dbx.files_get_temporary_link(scene.path_lower +'/preview.jpg').link
        context.append({'image_url': img})

    return render(request, 'flow/story_detail.html', context=context)


def home(request):
    context = {}
    text = "<h3> user: %s </h3> " % request.user
    text += """<a href="%s"> login to dbx </a><br/>""" % reverse('dropbox_auth_start')
    text += """<a href="%s"> logout </a><br/>""" % reverse('logout')

    if request.user.is_authenticated():

        app_key = request.user.dbx.access_token
        dbx = dropbox.Dropbox(app_key)
        text += """<br/> logged with: %s """ % request.session['dbx_oauth']

        for entry in dbx.files_list_folder('').entries:
            text +=" <br/> %s" % entry.name


    # return render(request, 'flow/index.html', context)
    return HttpResponse(text)