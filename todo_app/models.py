from django.db import models
from django.utils import timezone
from django.urls import reverse

def one_week_hence():
    """
    Return 7 days after at that time create
    """
    return timezone.now() + timezone.timedelta(days=7)

class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        """
        Return the URL for the particular data item
        """
        return reverse('list', args=[self.id])
    
    def __str__(self):
        """
        Standard Python way of creating a readable 
        repersentation of an object
        """
        return self.title

class TodoItem(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add = True)
    due_date = models.DateTimeField(default = one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete = models.CASCADE)
    def get_absolute_url(self):
        """"""
        return reverse(
            'item-update', args = [str[self.todo_list], str[self.id]]
        )
    def __str__(self):
        return f"{self.title}: due {self.due_date}"
    class Meta: 
        """
        Default ordering for ToDoItem record
        """
        ordering = ["due_date"]