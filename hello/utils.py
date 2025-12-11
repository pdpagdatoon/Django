from .models import Comment
from .forms import CommentForm

def handle_comment_section(request):
    page_id = request.path

    if request.method == "POST" and "comment_submit" in request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.page_identifier = page_id
            comment.save()
            form = CommentForm()  # reset form
    else:
        form = CommentForm()

    comments = Comment.objects.filter(page_identifier=page_id)
    return form, comments