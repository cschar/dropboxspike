from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from dropbox import dropbox

@login_required
def all_story(request):
    context = {}
    app_key = request.user.dbx.access_token
    dbx = dropbox.Dropbox(app_key)

    all_boards = []
    for board in dbx.files_list_folder('/stories/').entries:
        board_info = {'name': board.name,
                      'scenes': dbx.files_list_folder(board.path_lower+'/scenes').entries,
                      'submissions': dbx.files_list_folder(board.path_lower+'/submissions').entries,
                      }

        all_boards.append(board_info)

    context['all_boards'] =  all_boards

    return render(request, 'flow/allboard.html', context=context)

@login_required
def story(request, slug):
    app_key = request.user.dbx.access_token
    dbx = dropbox.Dropbox(app_key)

    context = []
    for scene in dbx.files_list_folder('/stories/'+slug).entries:
        img = dbx.files_get_temporary_link(scene.path_lower +'/preview.jpg').link
        context.append({'image_url': img})

    return render(request, 'flow/storyboard.html', context=context)