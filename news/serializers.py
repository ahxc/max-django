from rest_framework.serializers import HyperlinkedModelSerializer, Field, ModelSerializer
from datetime import datetime
from pytz import timezone

from .models import News
from max.settings import TIME_ZONE

# 覆写类
class TimestampField(Field):
  def to_representation(self, value):
    return value.timestamp()

  def to_internal_value(self, data):
    timestamp = float(data)
    no_tz = datetime.utcfromtimestamp(timestamp)
    # 不引入时区会告警
    return no_tz.astimezone(timezone(TIME_ZONE))

class NewsSerializer(HyperlinkedModelSerializer):
  released_timestamp = TimestampField(source='released_time')
  class Meta:
    model = News
    fields = [
      "id",
      "title",
      "released_timestamp",
      "views",
      "cover_url"
    ]

class DetailSerializer(ModelSerializer):
  released_timestamp = TimestampField(source='released_time')
  class Meta:
    model = News
    fields = [
      "id",
      "title",
      "text",
      "released_timestamp",
      "cover_url"
    ]