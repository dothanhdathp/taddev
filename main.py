def define_env(env):
    @env.macro
    def linkslide(title, link_html):
        return f'''<a href="javascript:void(0);" onclick="openSlide('http://localhost:65000/{link_html}')">⧉ {title}</a>'''
    
    @env.macro
    def slide(link_html, isfull=False):
        if isfull:
            return f'''<iframe src="http://localhost:65000/{link_html}" style="width: 100%; aspect-ratio: 16 / 9; border: none;" allowfullscreen></iframe>'''
        else:
            return f'''<div style="text-align: center;">
                <iframe 
                    src="http://localhost:65000/{link_html}" 
                    style="width: 960px; aspect-ratio: 16 / 9; border: none;"
                    allowfullscreen>
                </iframe>
            </div>'''
    
    @env.macro
    def book(title, book, page=""):
        if not page:
            html_page = ""
        else:
            # Kiểm tra xem page đã có đuôi .html chưa để tránh bị double (ví dụ: page.html.html)
            html_page = page if page.endswith(".html") else f"{page}.html"
		# Return
        return f'''[{title}](http://localhost:65000/book/{book}/{html_page})'''