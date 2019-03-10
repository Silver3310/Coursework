from django.db import models


class Question(models.Model):
    """
    Custom model for questions

    Attributes:
        question_text (string): question's text
        pub_date (datetime): the date of publishing a question
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def question_and_date(self):
        return "'{}' posted at {}".format(
            self.question_text,
            self.pub_date
        )

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    """
    Custom model for choices

    Attributes:
        question (Question): a question a choice belongs to
        choice_text (string): choice's text
        votes (int): the amount of votes a choice has
    """
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def add_vote(self):
        self.votes += 1
        self.save()

    def __str__(self):
        return self.choice_text
