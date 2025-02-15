from playwright.sync_api import expect
# Test 1: Otevření domovské stránky a ověření titulu
def test_open_homepage(page):
    # Otevření stránky
    page.goto("https://engeto.cz")
    
    # Ověření titulu
    assert "ENGETO" in page.title(), "Title does not contain 'ENGETO'"

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
    about_link = page.locator("nav>>text='O nás'")
    about_link.hover()
    story = page.locator("a:has-text('Příběh ENGETA')")
    expect(story).to_be_visible()

    # Kliknout na odkaz "O nás"
    story.click()
    
    # Ověřit, že URL obsahuje "o-nas"
    assert "o-nas" in page.url, "URL does not contain 'o-nas'"

# Test 4: Kontrola visibility tlačítka
def test_check_button_visibility(page):
    # Otevřít stránku
    page.goto("https://engeto.cz")
    
    # Přijetí cookie banneru (pokud existuje)
    accept_cookies(page)
    
    # Zkontrolovat, zda tlačítko "Login" existuje a je viditelné
    about_link = page.locator ("a.portal-link.h6.is_bold_700")
    # Ověřit, že odkaz existuje a je viditelný
    expect(about_link).to_be_visible()
    with page.expect_popup() as new_tab:
        about_link.click()
    new_page = new_tab.value 
    new_page.wait_for_load_state("domcontentloaded")
    assert new_page.url == "https://portal.engeto.com/lobby/sign-in"

# Test 5: Kontrola, zda je obrázek správně nahrán a je viditelný
def test_check_image_visibility(page):
    # Otevřít stránku
    page.goto("https://engeto.cz")
    
    # Přijetí cookie banneru (pokud existuje)
    accept_cookies(page)
    
    # Zkontrolovat, zda existuje obrázek s konkrétním alt textem
    image = page.locator('img[alt="ENGETO Academy"]')  # Replace "Logo" with the actual alt text of the image
    assert image.is_visible(), "Image with alt 'Logo' is not visible"

# Funkce pro přijetí cookie banneru
def accept_cookies(page):
    try:
        cookie_banner = page.get_by_role ("button", name="Chápu a přijímám!") # Text tlačítka na cookie banneru
        if cookie_banner.is_visible():
            cookie_banner.click()
    except Exception as e:
        print(f"Cookie banner not found or clickable: {e}")