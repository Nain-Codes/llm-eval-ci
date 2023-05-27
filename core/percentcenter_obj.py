from .forms import ProfitCenterForm
from .models import ProfitCenter,BusinessObjective,BizNeed



class ProfitCenterClass():
   
    #this method creates a new record in database
    def create(self, request):
        print(request.POST)
        form = ProfitCenterForm(request.POST)
        if form.is_valid():
            form.save()

    #this method finds the record from database using primary key and return that record
    def get(self, pk):
        profit_obj = ProfitCenter.objects.get(id = pk)
        return profit_obj

    #this method return all the records of profit center database
    def get_all(self):
        profit_objs = ProfitCenter.objects.all()
        return profit_objs

    #this method change the record 
    def change(self, request, profit_obj):
        form = ProfitCenterForm(request.POST, instance=profit_obj)
        if form.is_valid():
            form.save()

    #this method removes the particular record
    def remove(self, pk):
        profit_obj = ProfitCenter.objects.get(id = pk)
        profit_obj.delete()

    def getTree(self):
        profit_objs = ProfitCenter.objects.all()
        data = {
            'profitcenter': []
        }

        for profit_obj in profit_objs:
            profitcenter_data = {
                'profit_center_name': profit_obj.profit_center_name,
                'profit_center_desc': profit_obj.profit_center_desc,
                'businessObjective': []
            }

            business_objectives = BusinessObjective.objects.filter(profit_center_id=profit_obj.id)

            for business_objective in business_objectives:
                business_objective_data = {
                    'title': business_objective.title,
                    'boid': business_objective.boid,
                    'desc': business_objective.desc,
                    'metric': business_objective.metric,
                    'bizneed': []
                }

                biz_needs = BizNeed.objects.filter(boid=business_objective.boid)

                for biz_need in biz_needs:
                    biz_need_data = {
                        'desc': biz_need.desc,
                        'delivery_prod': biz_need.delivery_prod
                    }

                    business_objective_data['bizneed'].append(biz_need_data)

                profitcenter_data['businessObjective'].append(business_objective_data)

            data['profitcenter'].append(profitcenter_data)
        mydata =data['profitcenter']
        return mydata
