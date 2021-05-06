# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Stock(models.Model):
    class Meta:
        db_table = 'stocks'

    name = models.CharField(max_length=255)
    market = models.CharField(max_length=255)
    ipo_date = models.DateField()
    ipo_accepted_date = models.DateField()
    offering_price = models.IntegerField()
    provisional_price_min = models.IntegerField()
    provisional_price_max = models.IntegerField()
    offering_volume = models.IntegerField()
    sale_volume = models.IntegerField()
    file_1_url = models.CharField(max_length=255)
    file_2_url = models.CharField(max_length=255)
    file_3_url = models.CharField(max_length=255)
    file_4_url = models.CharField(max_length=255)
    file_5_url = models.CharField(max_length=255)
