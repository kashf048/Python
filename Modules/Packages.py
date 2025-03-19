# import Modules.ecommerce.sales as sales
# import ecommerce.sales
from Modules.ecommerce.shopping.sales import calc_tax
from Modules.ecommerce.shopping import sales

# ecommerce.sales.calc_tax()    # noisy
calc_tax()
sales.calc_shipping()
sales.calc_tax()