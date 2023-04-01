import sys
 # setting path
sys.path.append('../controllers')



# from controllers.recommendation import 


def crop_prediction_routes(api):
    api.add_reource()
    api.add_resource(cropprice,'/api/cropprice/<name>')