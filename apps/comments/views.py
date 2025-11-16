from django.shortcuts import render, redirect
from .models import Comment
from apps.quiz.models import Quiz
from django.contrib.auth.decorators import login_required


# MENAMPILKAN DAFTAR KOMENTAR UNTUK TES TERTENTU #
def comment_list(request, quiz_id):
    """
    Menampilkan semua komentar yang terkait dengan quiz tertentu.
    Komentar diurutkan berdasarkan tanggal pembuatan (terbaru di atas).
    """
    comments = Comment.objects.filter(quiz_id=quiz_id).order_by('-created_at')
    quiz = Quiz.objects.get(id=quiz_id)
    return render(request, 'comments/comment_list.html', {
        'comments': comments,
        'quiz': quiz
    })


# MENAMBAHKAN KOMENTAR BARU UNTUK TES TERTENTU #
def add_comment(request):
    """
    Menyimpan komentar baru untuk quiz tertentu.
    Jika user login, komentar disimpan dengan user.
    Jika tidak, komentar disimpan sebagai guest.
    """
    if request.method == 'POST':
        content = request.POST.get('content')
        quiz_id = request.POST.get('quiz_id')
        if request.user.is_authenticated:
            Comment.objects.create(
                user=request.user,
                content=content,
                quiz_id=quiz_id
            )
        else:
            username = request.POST.get('guest_username')
            Comment.objects.create(
                guest_username=username,
                content=content,
                quiz_id=quiz_id
            )
        return redirect(f'/comments/{quiz_id}/')
    

def comment_index(request):
    quizzes = Quiz.objects.all()
    return render(request, 'comments/index.html',{
        'quizzes': quizzes
    })