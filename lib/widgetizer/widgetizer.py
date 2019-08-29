from wct_app.config.wct_config import WCT_SECRET_SAUCE, PATH_TO_DATA_FILE

class Widgetizer:
    def __init__(self, widget_material):
        self.widget_material = widget_material
        self.secret_sauce = int(WCT_SECRET_SAUCE)
        self.widget = ''.join(['(ಠ_ಠ){}(ಠ_ಠ)\n'.format(self.widget_material) \
        for _ in range(self.secret_sauce)])
        
    def save_widget(self):

        if type(self.widget_material) == str:
            with open('{}/widget.store.str'.format(PATH_TO_DATA_FILE), 'a') as outfile:
                outfile.write('\n\n{}'.format(self.widget))

        if type(self.widget_material) == int:

            with open('{}/widget.store.int'.format(PATH_TO_DATA_FILE), 'a') as outfile:
                outfile.write('\n\n{}'.format(self.widget))
