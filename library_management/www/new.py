import frappe
from library_management.utils import paginate

def get_context(context):
    #print(f"\n\n\n{frappe.form_dict}\n\n{frappe.form_dict.hello}")
    #properties = frappe.db.sql("""SELECT name, author FROM `tabArticle` ORDER BY name ASC;""",
    #    as_dict=True)
    
    page = frappe.form_dict.page
    pagination = paginate('Article', page)
    context.articles=pagination.get('articles')
    context.prev = pagination.get('prev')
    context.next = pagination.get('next')

    return context
