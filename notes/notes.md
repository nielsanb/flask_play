# Notes to creating a quick 

## H2
### H3
**bold text**
*italic text*

> blockquote

```sql
select * from table
```

1. item
2. item
3. item

---
Horizontal rules 
---

## H2 What I did:
0. Simplest flask website possible

1. Picking up data with the backend
    URL
    QUERYSTRING
    POST REQUEST
    
1. Redirecting URLs to other functions
    WITH PASSING ALONG THE VARIABLE

2. Rendering a simple html template with the return render_template() function

3. Rendering html templates
    USING JINJA IN TEMPLATES - VARIABLES (to add variables/lists, for and if}
    JINJA LISTS AND LOOPS
    TEMPLATE INHERITANCE with {% block name %} and {% extends "base.html"%}
    ADDING CSS via a .css file
    ADDING BOOTSTRAP (i.e. external style framework)
    ADDING REUSABLE BOOTSTRAP NAVBAR with BASE and CHILD

4. GET and POST
    GET -> not-secure
    POST -> sends secure information (e.g. form data) that is encrypted, and that cannot be seen from either ends, and is not stored on the actual server (unless we go send it to a database!).