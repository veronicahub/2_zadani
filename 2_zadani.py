#1 Test 1: Otevření domovské stránky a ověření titulu
def test_open_homepage(page):  
    # Otevření stránky
    page.goto("https://engeto.cz")
    
    # Ověření titulu
    assert "Engeto" in page.title()

# Test 2: Kontrola hlavního nadpisu
def test_check_main_heading(page):
    # Otevřít stránku
    page.goto("https://engeto.cz")

    # Zkontrolovat, zda hlavní nadpis (h1) existuje a je viditelný
    main_heading = page.locator("h1")
    assert main_heading.is_visible()

# Test 3: Kliknutí na odkaz a ověření navigace
def test_navigation_to_about(page):
    # Otevřít stránku
    page.goto("https://engeto.cz")

    # Kliknout na odkaz "O nás" (pokud existuje)
    page.locator('a:has-text("O nás")').click()

    # Ověřit, že URL obsahuje "o-nas"
    assert "o-nas" in page.url

    #Test 4: Kontrola visibility buttonu
def test_check_button_visibility(page):
    # Otevřít stránku
    page.goto("https://engeto.cz")
    
    # Zkontrolovat, zda tlačítko "Login" existuje a je viditelné
    login_button = page.locator('button:has-text("Login")')
    assert login_button.is_visible()

    #Test 5: Kontrola, zda je obrázek správně nahrán a je viditelný
def test_check_image_visibility(page):
    # Otevřít stránku
    page.goto("https://engeto.cz")
    
    # Zkontrolovat, zda existuje obrázek s konkrétním alt textem
    image = page.locator('img[alt="Logo"]')  # Replace "Logo" with the actual alt text of the image
    assert image.is_visible()  # Verify that the image is visible
