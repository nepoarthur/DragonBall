from django.views.generic import FormView
from .models import Enemy, Hero, Feature, Price, Testimonial, OtherImage
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['all_enemies'] = Enemy.objects.order_by('?').all()
        context['all_prices'] = Price.objects.all()
        context['all_heroes'] = Hero.objects.all()
        context['all_testimonials'] = Testimonial.objects.all()
        context['all_features_leftside'] = Feature.objects.all()[:3]
        context['all_features_rightside'] = Feature.objects.all()[3:]
        context['all_other_images'] = OtherImage.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email sent successfully')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Error trying to send message.')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

