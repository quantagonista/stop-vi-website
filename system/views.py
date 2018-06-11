# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.
from django.utils import translation
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'system/index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            user_language = self.request.POST.get('lang')
            translation.activate(user_language)

        return render(request, self.template_name)


class HelpView(TemplateView):
    template_name = 'system/help.html'

    def get_context_data(self, **kwargs):
        context = {}
        items = [
            {
                'name': 'Ассоциация кризисных центров Кыргызстана'.upper(),
                'address': 'ул. Киевская д. 27 кв. 401, г. Бишкек, Кыргызстан',
                'phone': '+996 (312) 66-15-92',
                'email': 'association.kg@gmail.com',
                'description': 'В состав Ассоциации Кризисных Центров входят 12 кризисных центров и НПО, куда Вы можете обратиться за помощью'
            },

            {
                'name': 'Кризисный центр «Алтынай»'.upper(),
                'address': 'Иссык — Кульская область, г. Чолпон-Ата',
                'phone': '+996 (03943) 4-41-37',
                'email': 'altynai1951@mail.ru',
                'description': 'Сфера деятельности:\nКонсультации юриста, психолога, врача-гинеколога;\nПредоставление убежища;\nПредставление интересов потерпевших в суде;\nТелефон доверия +996 (03934) 4 41 37'
            },

            {
                'name': '«Ак-Журок» — морально-психологический центр'.upper(),
                'address': 'г. Ош',
                'phone': '+996 (3222) 2-97-57',
                'email': 'kjurok05@rambler.ru',
                'description': 'Сфера деятельности: Оказание морально — психологической помощи женщинам, пострадавшим от насилия; Телефон доверия; Группы поддержки; Информационно — образовательная работа с населением.'
            },

            {
                'name': 'Кризисный центр «Акылкарачач»'.upper(),
                'address': 'Ошская область, Алайский район, с. Гульча',
                'phone': '+996 (03234) 2 60 33 , 2-61-31',
                'email': 'ene-naz@mail.ru',
                'description': 'Сфера деятельности: Очные и выездные консультации психолога и юриста; Телефон доверия; Предоставление кредитов для женщин, потерпевших насилие; Предоставление убежища.'
            },

            {
                'name': 'Кризисный центр «Аруулан» (Ошский областной ЦЖИ «Аялзат»)'.upper(),
                'address': 'г. Ош',
                'phone': '+996 (03222) 5-56-08',
                'email': 'ayalzat@netmail.kg',
                'description': 'Сфера деятельности: Телефон доверия; Очные консультации психолога, юриста, гинеколога; Предоставление убежища.'
            },

            {
                'name': '«Даршайым» — Центр Профилактики Насилия'.upper(),
                'address': 'г. Бишкек',
                'phone': '+996 (0312) 64-93-50',
                'email': 'darshayim@mail.ru , mairash_1955@mail.ru',
                'description': 'Сфера деятельности: консультационная; обучающая; информационная.'
            },

            {
                'name': 'Кризисный центр «Жаныл мырза» (Общественный фонд «Омур Булагы»)'.upper(),
                'address': 'Баткенская область, г. Баткен',
                'phone': '+996 (03622) 2-20-27',
                'email': 'kalybek2003@mail.ru',
                'description': 'Сфера деятельности: Телефон доверия; Очные консультации психолога, юриста; Предоставление убежища.'
            },

            {
                'name': 'Кризисный центр «Каниет» (Ассоциация «Женщины-лидеры Джалал-Абада»)'.upper(),
                'address': 'г. Джалал-Абад',
                'phone': '+996 (03722) 5-50-84',
                'email': 'j_saralaeva@mail.ru',
                'description': 'Сфера деятельности: Телефон доверия; Очные консультации психолога, юриста, врача-гинеколога; Предоставление убежища.'
            },

            {
                'name': '«Маана» (Общественный фонд «Аялзат»)'.upper(),
                'address': 'г. Талас',
                'phone': '+996 (03422) 5-38-18 (р.), 5-55-81',
                'email': 'ayalzat@mail.ru',
                'description': 'Сфера деятельности: Телефон доверия; Консультации: юриста, психолога, врача; Предоставление временного убежища (до 10 дней); Представление интересов в суде; Оказание материальной и финансовой помощи; Трудоустройство пострадавших от насилия; Определение детей пострадавших от насилия в школы, интернаты; Просветительская и информационная деятельность.'
            },

            {
                'name': 'Общественное объединение «Мээрбан»'.upper(),
                'address': 'г. Ош',
                'phone': '+996 (03222) 7-40-06 , 7-40-17',
                'email': 'meerban.osh@mail.ru',
                'description': 'Сфера деятельности: Консультационная; Обучающая; Информационная; Проведение эдвокаси кампаний.'
            },

            {
                'name': 'Кризисный центр «Тендеш»'.upper(),
                'address': 'г. Нарын',
                'phone': '+996 (03522) 5-37-70, 5-02-70 (ф.)',
                'email': 'ngo-tendesh@rambler.ru',
                'description': 'Сфера деятельности: Телефон доверия; Очные консультации: психолога, юриста, врача; Предоставление убежища.'
            },

            {
                'name': '«Сезим» кризисный психологический центр для женщин и семьи'.upper(),
                'address': 'г. Бишкек',
                'phone': '+996 (0312) 51-26-40',
                'email': 'sezim2008@gmail.com',
                'description': 'Сфера деятельности: Круглосуточный телефон доверия; Убежище для женщин; Прием пострадавших от семейного насилия (прием с детьми не новорожденными); Консультации психолог, юриста, терапевт; Информационно — образовательная работа с населением.'
            },

            {
                'name': 'Кризисный центр «Шанс»'.upper(),
                'address': 'г. Бишкек',
                'phone': '+996 (0312) 43-53-01',
                'email': 'chance-cc@mail.ru',
                'description': 'Сфера деятельности: Телефон доверия; Очные консультации психолога, юриста; Медицинская амбулаторная помощь; Издательская деятельность; Информационно — образовательная работа с населением'
            },

        ]
        context = {'items': items}
        return context
