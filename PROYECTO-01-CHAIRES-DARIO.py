from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches


#TO LIST ALL ADMIN USERS (TO SHOW STATUS REPORT) AND CLIENT USERS (DENY ACCESS)

user_password = [["Javier","241097"],["Vanessa","102497"],["Daniel","971024"]]

admin = 0
while admin != 1:
 inpt_user = input("Enter user name: ")
 inpt_password = input("Enter password: ")
 #Login autenthication----------------------------------------
 for user in user_password:
  if user[0] == inpt_user and user[1] == inpt_password:
    admin = 1
    break  
 if admin == 1:
  print("Welcome to status report")
 else:
  print("You are not an available admin")
  print("Try again")
 #Select desired option---------------------------------------
while admin == 1: 
  print("select an option: \n 1) Count total of ID products\n 2) Count total of products\n 3) List the 50 most and less selled products\n 4) List the 100 most and less searched products\n 5) List the 20 best and worst rated products\n 6) Check monthly/yearly income\n 7) Check mean sells per month\n 8) Check best selling months\n 9) Exit")
        
  opt_inpt = input()
  if opt_inpt == "1":
    print("\n******\nTotal ID products:\n******\n")
    print(len(lifestore_products))
    
  if opt_inpt == "2":
    total_products = 0
    for product in lifestore_products:
      total_products += product[4]
    print("\n******\nThe total number of products is:\n******\n", total_products,"\n")

  
  if opt_inpt == "3":
     total_sales = []
     for product in lifestore_products:
       counter_sales = 0
       for sale in lifestore_sales:
         if product[0] == sale[1]:
           counter_sales += 1
       ideal_format = [product[1], counter_sales]
       total_sales.append(ideal_format)
     #print("\n The sales list is:\n ", total_sales)
     ordered_sales = []
     while total_sales:
       minimo = total_sales[0][1]
       actual_list = total_sales[0]
       for sale in total_sales:
         if sale[1] < minimo:
           minimo = sale[1]
           actual_list = sale
       ordered_sales.append(actual_list)
       total_sales.remove(actual_list)
     print("\n******\n The 50 less sold products are:\n******\n")
     for order1 in ordered_sales[0:50]:
       print(order1[0],"\n")
     print("\n******\n The 50 most sold products are:\n******\n")
     for order1 in ordered_sales[46:96]:
       print(order1[0],"\n")
    

  if opt_inpt == "4":
     total_searches =[]
     for product in lifestore_products:
       counter_searches = 0
       for searches in lifestore_searches:
         if product[0] == searches[1]:
           counter_searches += 1
       search_format = [product[1], counter_searches]
       total_searches.append(search_format)
     #print("\n The search list is:\n ", total_searches)
     ordered_searches = []
     while total_searches:
       minimo = total_searches[0][1]
       actual_search = total_searches[0]
       for search in total_searches:
         if search[1] < minimo:
           minimo = search[1]
           actual_search = search
       ordered_searches.append(actual_search)
       total_searches.remove(actual_search)
     print("\n******\n The 50 less searched products are:\n******\n")
     for order2 in ordered_searches[0:50]:
       print(order2[0],"\n")
     print("\n******\n The 50 most searched products are:\n******\n")
     for order2 in ordered_searches[46:96]:
         print(order2[0],"\n")


  if opt_inpt == "9":
      exit(1)
