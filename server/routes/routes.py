import sys
 # setting path
sys.path.append('../controllers')

from controllers.recommendation import Recommendations, ClientRecommendation, ItemRecommendation
from controllers.orders import Orders, Client


def recommendations_routes(api):
    api.add_resource(Recommendations,"/api/recommendations/<num>");
    api.add_resource(ClientRecommendation,'/api/clientrecommendation');
    api.add_resource(ItemRecommendation,"/api/itemrecommendation");

    api.add_resource(Orders,"/api/orders");
    api.add_resource(Client,"/api/client");