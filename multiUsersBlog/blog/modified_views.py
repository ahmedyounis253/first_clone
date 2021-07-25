from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
class createpost(LoginRequiredMixin ,CreateView):
    def form_valid(self, form) :
        print(self.request.user)
        object=form.save(commit=False)
        object.author=self.request.user
        object.create_time=timezone.now()
        object.save()

        return super(createpost,self).form_vaild(form)
