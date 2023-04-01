import sys
 # setting path
sys.path.append('../controllers')

from controllers.recommendation import Recommendations, ClientRecommendation, ItemRecommendation


def recommendations_routes(api):
    api.add_resource(Recommendations,"/api/recommendations/<num>");
    api.add_resource(ClientRecommendation,'/api/clientrecommendation');
    api.add_resource(ItemRecommendation,"/api/itemrecommendation");