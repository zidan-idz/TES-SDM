from django.db import models
from django.contrib.auth.models import User

# MODEL QUIZ
class Quiz(models.Model):
    """
    Model untuk menyimpan data tes.
    - title: judul tes
    - time_limit: batas waktu pengerjaan tes (dalam menit)
    - kkm_score: nilai minimal kelulusan
    """
    title = models.CharField(max_length=255)
    time_limit = models.IntegerField(default=2)
    kkm_score = models.IntegerField(default=70)

    def __str__(self):
        return self.title


# MODEL QUESTION
class Question(models.Model):
    """
    Model untuk menyimpan pertanyaan tes.
    - quiz: relasi ke tes terkait
    - text: isi pertanyaan
    - option_a..d: pilihan jawaban
    - correct_answer: jawaban yang benar (A/B/C/D)
    - score: nilai pertanyaan
    """
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1)
    score = models.IntegerField(default=10)

    def __str__(self):
        return self.text
    

# MODEL RESULT
class Result(models.Model):
    """
    Model untuk menyimpan hasil quiz.
    - user: jika login, relasi ke User
    - guest_username: jika guest, nama pengunjung
    - quiz: tes yang diikuti
    - score: skor yang didapat
    - completed_at: waktu selesai tes
    """
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    guest_username = models.CharField(max_length=15, null=True, blank=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user:
            return f'{self.user.username} - {self.score}'
        return f'Guest {self.guest_username} - {self.score}'
