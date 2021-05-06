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

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Stock

def index(request: HttpRequest) -> HttpResponse:
    # data = Stock.objects.exclude(offering_price=None).all()
    data = Stock.objects.exclude(offering_volume=None).order_by("-ipo_date")
    params = { 'data': data }
    return render(request, 'polls/index.html', params)
