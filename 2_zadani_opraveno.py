# Test 1: Otevření domovské stránky a ověření titulu
def test_open_homepage(page):
    # Otevření stránky
    page.goto("https://engeto.cz")
    
    # Přijetí cookie banneru (pokud existuje)
    accept_cookies(page)
    
    # Ověření titulu
    assert "Engeto" in page.title(), "Title does not contain 'Engeto'"

# Test 2: Kontrola hlavního nadpisu
def test_check_main_heading(page):
    # Otevřít stránku
    page.goto("https://engeto.cz")
    
    # Přijetí cookie banneru (pokud existuje)
    accept_cookies(page)
    
    # Zkontrolovat, zda hlavní nadpis (h1) existuje a je viditelný
    main_heading = page.locator("h1")
    assert main_heading.is_visible(), "Main heading (h1) is not visible"

# Test 3: Kliknutí na odkaz a ověření navigace
def test_navigation_to_about(page):
    # Otevřít stránku
    page.goto("https://engeto.cz")
    
    # Přijetí cookie banneru (pokud existuje)
    accept_cookies(page)
    
    # Ověřit, zda odkaz "O nás" existuje
    about_link = page.locator('a:has-text("O nás")')
    assert about_link.is_visible(), "Link 'O nás' is not visible"
    
    # Kliknout na odkaz "O nás"
    about_link.click()
    
    # Ověřit, že URL obsahuje "o-nas"
    assert "o-nas" in page.url, "URL does not contain 'o-nas'"

# Test 4: Kontrola visibility tlačítka
def test_check_button_visibility(page):
    # Otevřít stránku
    page.goto("https://engeto.cz")
    
    # Přijetí cookie banneru (pokud existuje)
    accept_cookies(page)
    
    # Zkontrolovat, zda tlačítko "Login" existuje a je viditelné
    login_button = page.locator('button:has-text("Login")')
    assert login_button.is_visible(), "Login button is not visible"

# Test 5: Kontrola, zda je obrázek správně nahrán a je viditelný
def test_check_image_visibility(page):
    # Otevřít stránku
    page.goto("https://engeto.cz")
    
    # Přijetí cookie banneru (pokud existuje)
    accept_cookies(page)
    
    # Zkontrolovat, zda existuje obrázek s konkrétním alt textem
    image = page.locator('img[alt="Logo"]')  # Replace "Logo" with the actual alt text of the image
    assert image.is_visible(), "Image with alt 'Logo' is not visible"

# Funkce pro přijetí cookie banneru
def accept_cookies(page):
    try:
        cookie_banner = page.locator('button:has-text("Přijmout vše")')  # Text tlačítka na cookie banneru
        if cookie_banner.is_visible():
            cookie_banner.click()
    except Exception as e:
        print(f"Cookie banner not found or clickable: {e}")