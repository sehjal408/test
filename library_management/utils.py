import frappe

def paginate(doctype, page=0):
    prev, next = 0, 0
    conditions = " "
    query = f"""SELECT name, author, image, status, route 
        FROM `tabArticle` {conditions} ORDER BY name ASC """

    if(page):
        page = int(page)
        articles = frappe.db.sql(query+f"""LIMIT {(page*4)-4 }, 4;""", as_dict=True)
        next_set = frappe.db.sql(query+f"""LIMIT {page*4}, 4;""", as_dict=True)
        if(next_set):
            prev, next = page-1, page+1
        else:
            prev, next = page-1, 0
    else:
        count = frappe.db.sql("""SELECT COUNT(name) as count FROM `tabArticle`;""", as_dict=True)[0].count
        if(count>4):
            prev, next = 0, 2
        else:
            pass
        articles = frappe.db.sql(query+"""LIMIT 4;""", as_dict=True) 
    return {
        'articles' : articles,
        'prev': prev,
        'next': next,
    }