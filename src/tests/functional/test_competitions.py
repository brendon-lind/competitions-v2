import os

from django.urls import reverse

from factories import UserFactory
from ..utils import SeleniumTestCase


class TestCompetitions(SeleniumTestCase):
    def setUp(self):
        super().setUp()
        self.user = UserFactory(password='test')
        self.login(self.user.username, 'test')

    def _upload_competition(self, competition_zip_path):
        """Creates a competition and waits for success message.

        :param competition_zip_path: Relative to test_files/ dir
        """
        self.get(reverse('competitions:upload'))
        self.find('input[ref="file_input"]').send_keys(os.path.join(self.test_files_dir, competition_zip_path))
        self.circleci_screenshot(name='uploading_comp.png')

        assert self.element_is_visible('div .ui.success.message')

        comp = self.user.competitions.first()
        comp_url = reverse("competitions:detail", kwargs={"pk": comp.id})
        self.find(f'a[href="{comp_url}"]').click()
        self.assert_current_url(comp_url)

    def test_upload_v15_competition(self):
        self._upload_competition('competition_15.zip')

    def test_upload_v2_competition(self):
        self._upload_competition('competition.zip')
