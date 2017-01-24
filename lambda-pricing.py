import json
###AWS Usage Charges or Bill Amount
def lambda_handler(event, context):
    bill = float(event["MonthlyBill"])
    


## BASIC PLAN ###
    if bill >= 0:
        basic_plan_cost = {'Basic Plan ' : 'Included'}
        


### DEV SUPPORT PLAN ###
    devbase = float(29.00)
    if (.03 * bill) >= 29:
        dev_plan_cost = {'Developer Support Cost is $': round((.03 * bill),2)}
    else:
        dev_plan_cost = {'Developer Support Cost is $':(devbase)}


### BUSINESS SUPPORT PLAN ###
    businessbase = float(100.00)
    # a = 0.1 * bill
    # b = 1000 + (0.07 * (bill-10000))
    # c = 1000 + 4900 + (0.05 * (bill-80000))
    # d = 1000 + 4900 +  5100 + (0.03 * (bill-250000))

    if 0 <= bill < 10000:
        if businessbase > (0.1 * bill):
            business_plan_cost = {'Business Support Cost is $': (businessbase)}
        else:
            business_plan_cost = {'Business Support Cost is $': round((0.1 * bill),2)}
    elif 10000 <= bill < 80000:
        business_plan_cost = {'Business Support Cost is $': round((1000 + (0.07 * (bill - 10000))),2)}
    elif 80000 <= bill < 250000:
        business_plan_cost = {'Business Support Cost is $': round((1000 + 4900 + (0.05 * (bill - 80000))),2)}
    elif bill >= 250000:
        business_plan_cost = {'Business Support Cost is $': round((1000 + 4900 + 5100 + (0.03 * (bill - 250000))),2)}


### ENTERPRISE SUPPORT PLAN ###
    enterprisebase = float(15000.00)
    # a = 0.1 * bill
    # b = 15000 + (0.07 * (bill-150000))
    # c = 15000 + 24500 + (0.05 * (bill-500000))
    # d = 15000 + 24500 +  25000 + (0.03 * (bill-1000000))

    if 0 <= bill < 150000:
        if enterprisebase > 0.1 * bill:
            enterprise_plan_cost = {'Enterprise Support Cost is $' : enterprisebase}
        else:
            enterprise_plan_cost = {'Enterprise Support Cost is $': round((0.1 * bill),2)}
    elif 150000 <= bill < 500000:
        enterprise_plan_cost = {'Business Support Cost is $': round((15000 + (0.07 * (bill - 150000))),2)}
    elif 500000 <= bill < 1000000:
        enterprise_plan_cost = {'Enterprise Support Cost is $': round((15000 + 24500 + (0.05 * (bill - 500000))),2)}
    elif bill >= 1000000:
        enterprise_plan_cost = {'Enterprise Support Cost is $': round((15000 + 24500 + 25000 + (0.03 * (bill - 1000000))),2)}

    #return json.dumps(basic_plan_cost),json.dumps(dev_plan_cost),json.dumps(business_plan_cost),json.dumps(enterprise_plan_cost)
    return basic_plan_cost,dev_plan_cost,business_plan_cost,enterprise_plan_cost