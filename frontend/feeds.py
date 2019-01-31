# pylint: disable-msg=R0201

from django.urls import reverse
from django.contrib.syndication.views import Feed

from frontend.models import EDID


class UploadedEDIDsFeed(Feed):
    title = "EDID.tv"
    link = "/"
    description = "Latest uploaded EDIDs."
    description_template = 'feeds/edid_description.html'

    def feed_url(self):
        return reverse('uploaded-feed')

    def items(self):
        return EDID.objects.order_by('-created')[:10]

    def item_pubdate(self, item):
        return item.created

    def item_title(self, item):
        return '%s %s' % (item.manufacturer.name,
                          item.manufacturer_serial_number)


class UpdatedEDIDsFeed(Feed):
    title = "EDID.tv"
    link = "/"
    description = "Latest updated EDIDs."
    description_template = 'feeds/edid_description.html'

    def feed_url(self):
        return reverse('updated-feed')

    def items(self):
        return EDID.objects.order_by('-modified')[:10]

    def item_pubdate(self, item):
        return item.modified

    def item_title(self, item):
        return '%s %s' % (item.manufacturer.name,
                          item.manufacturer_serial_number)
