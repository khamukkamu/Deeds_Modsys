from compiler import *
register_plugin(__name__)

color_crazy_news = color_bad_news
plugin_test_message = "@This is a plugin test injection!"

injection = {
  'display_test_message' : [
    (display_message, plugin_test_message, color_crazy_news),
  ],
}
