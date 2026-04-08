import re

file_path = 'c:/Users/user/Downloads/Pitch/Pitch/pitch.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Index
index_updates = {
    r'08</div>\s*<div style="padding-top:0.25rem;">\s*<div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Galería Visual': 
    '09</div>\n              <div style="padding-top:0.25rem;">\n                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Galería Visual',
    
    r'11</div>\s*<div style="padding-top:0.25rem;">\s*<div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Público Objetivo': 
    '12</div>\n              <div style="padding-top:0.25rem;">\n                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Público Objetivo',

    r'12</div>\s*<div style="padding-top:0.25rem;">\s*<div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Ecosistema Web': 
    '13</div>\n              <div style="padding-top:0.25rem;">\n                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Ecosistema Web',

    # Also for "Ecosistema Web INTERACTIVO"
    r'14</div>\s*<div style="padding-top:0.25rem;">\s*<div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">La Revista': 
    '14</div>\n              <div style="padding-top:0.25rem;">\n                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">La Revista',

    r'15</div>\s*<div style="padding-top:0.25rem;">\s*<div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Empaque 3D': 
    '16</div>\n              <div style="padding-top:0.25rem;">\n                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Empaque 3D',

    r'16</div>\s*<div style="padding-top:0.25rem;">\s*<div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Material POP': 
    '17</div>\n              <div style="padding-top:0.25rem;">\n                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Material POP',

    r'17</div>\s*<div style="padding-top:0.25rem;">\s*<div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Estrategia': 
    '18</div>\n              <div style="padding-top:0.25rem;">\n                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Estrategia',

    r'18</div>\s*<div style="padding-top:0.25rem;">\s*<div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Roles': 
    '19</div>\n              <div style="padding-top:0.25rem;">\n                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Roles',

    r'19</div>\s*<div style="padding-top:0.25rem;">\s*<div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Resultados': 
    '20</div>\n              <div style="padding-top:0.25rem;">\n                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Resultados'
}

for k, v in index_updates.items():
    text = re.sub(k, v, text)


# 2. Add New Slide 8
new_slide = """
    <!-- ══ SLIDE NUEVA: QR MANUAL DE MARCA ══ -->
    <section class="slide tc center-slide" style="background:var(--purple); padding:0;">
      <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; gap:2.5rem; width:100%;">
        <h2 style="font-size:4.5vw; color:#fff; text-align:center; font-family:'Montserrat'; font-weight:900;">Escanea para ver el<br>Manual de Marca<br>NUKAK.</h2>
        <div style="width:40vh; height:40vh; background:#fff; padding:1.5rem; border-radius:16px; box-shadow:0 15px 35px rgba(0,0,0,0.3);">
          <img src="foticx/QR manual nukak.png" style="width:100%; height:100%; object-fit:contain;">
        </div>
      </div>
    </section>
"""

# Find place to insert (before slide 8)
# "<!-- ══ SLIDE 08: GALERÍA 1 ══ -->"
text = text.replace("<!-- ══ SLIDE 08: GALERÍA 1 ══ -->", new_slide + "\n    <!-- ══ SLIDE 08: GALERÍA 1 ══ -->")

# 3. Slide 8 (now 9), 9 (now 10), 10 (now 11) styles
# Remove padding, set img cover
text = re.sub(r'<!-- ══ SLIDE 08: GALERÍA 1 ══ -->\s*<section class="slide td center-slide" style="padding: 0 2vw; position:relative;">\s*<img src="foticx/logo\.svg" style="width:100%; height:94vh; object-fit:contain; z-index:1;">',
              '<!-- ══ SLIDE 08: GALERÍA 1 ══ -->\n    <section class="slide td center-slide" style="padding: 0; position:relative;">\n      <img src="foticx/logo.svg" style="width:100vw; height:100vh; object-fit:cover; z-index:1;">', text)

text = re.sub(r'<!-- ══ SLIDE 09: GALERÍA 2 ══ -->\s*<section class="slide td center-slide" style="padding: 0 2vw;">\s*<img src="foticx/paleta\.svg" style="width:100%; height:94vh; object-fit:contain;">',
              '<!-- ══ SLIDE 09: GALERÍA 2 ══ -->\n    <section class="slide td center-slide" style="padding: 0;">\n      <img src="foticx/paleta.svg" style="width:100vw; height:100vh; object-fit:cover;">', text)

text = re.sub(r'<!-- ══ SLIDE 10: GALERÍA 3 ══ -->\s*<section class="slide td center-slide" style="padding: 0 2vw;">\s*<img src="foticx/tipografia\.svg" style="width:100%; height:94vh; object-fit:contain;">',
              '<!-- ══ SLIDE 10: GALERÍA 3 ══ -->\n    <section class="slide td center-slide" style="padding: 0;">\n      <img src="foticx/tipografia.svg" style="width:100vw; height:100vh; object-fit:cover;">', text)

# Remove the QR box from old Slide 8
qr_box_pattern = r'<div\s*style="position:absolute; bottom:5vh; right:5vw; z-index:10; display:flex; flex-direction:row; align-items:center; gap:1rem; background:rgba\(0,0,0,0\.5\); padding:1rem; border-radius:12px; backdrop-filter:blur\(5px\); border:1px solid rgba\(255,255,255,0\.1\); box-shadow:0 10px 30px rgba\(0,0,0,0\.5\);">.*?</div>\s*</section>'
text = re.sub(qr_box_pattern, '</section>', text, flags=re.DOTALL)

# 4. Update the Ghost Tags and Normal tags numbers
# We need to increment the numbers 08 and above
# Slide numbers to update: 19->20, 18->19, ..., 08->09
for i in range(19, 7, -1):
    old_n = str(i).zfill(2)
    new_n = str(i+1).zfill(2)
    
    # 1. HTML comments SLIDE xx:
    text = text.replace(f"<!-- ══ SLIDE {old_n}:", f"<!-- ══ SLIDE {new_n}:")
    # 2. Ghost tags
    text = text.replace(f'<div class="ghost" style="color:rgba(0,0,0,.04);">{old_n}</div>', f'<div class="ghost" style="color:rgba(0,0,0,.04);">{new_n}</div>')
    text = text.replace(f'<div class="ghost" style="color:rgba(0,0,0,.03);">{old_n}</div>', f'<div class="ghost" style="color:rgba(0,0,0,.03);">{new_n}</div>')
    text = text.replace(f'<div class="ghost ghost-w">{old_n}</div>', f'<div class="ghost ghost-w">{new_n}</div>')
    # 3. Tags
    text = text.replace(f'<span class="tag rv d1">{old_n} —', f'<span class="tag rv d1">{new_n} —')
    text = text.replace(f'<span class="tag tag-w rv d1">{old_n} —', f'<span class="tag tag-w rv d1">{new_n} —')


# 5. Fix diapositiva 5 (mujernukak)
# old: <img src="foticx/mujernukak.png" style="position:absolute; bottom:0; right:7vw; width:45vw; max-height:85vh; object-fit:contain; object-position:center bottom; z-index:0;">
old_nukak = 'right:7vw; width:45vw; max-height:85vh'
new_nukak = 'right:2vw; width:55vw; max-height:95vh'
text = text.replace(old_nukak, new_nukak)

# 6. Change Slide 19 (Old 19, new 20 -> Resultados)
# "cambia todos los textos deben ser negros NO grises los grises puedes cambiarlos por rojos y no pongas verdes tampoco solo rojos"
# Old 19 is now 20!
# Its content:
# <h4 style="font-family:'Montserrat'; font-size:1vw; font-weight:900; color:#fff; margin-bottom:1rem; text-transform:uppercase;">Estimado de Resultados</h4>
# <p style="font-size:0.6vw; color:#888; text-transform:uppercase; letter-spacing:0.1em; margin-top:0.3rem;">Ventas (Mes 1)</p>
# <td style="padding:1rem; color:var(--green); font-weight:bold;">Proyecto</td>
# etc... We must do it carefully.
if "<!-- ══ SLIDE 20: RESULTADOS" in text or "<!-- ══ SLIDE 20" in text:
    # Extract slide 20 block to modify it independently
    start_idx = text.find('<!-- ══ SLIDE 20')
    end_idx = text.find('<!-- ══ SLIDE 21')
    if end_idx == -1: end_idx = len(text)
    
    slide_20_part = text[start_idx:end_idx]
    
    # Text colors
    # color:#fff -> color:#000
    slide_20_part = slide_20_part.replace('color:#fff;', 'color:#000;')
    # color:#aaa -> color:var(--red)
    slide_20_part = slide_20_part.replace('color:#aaa;', 'color:var(--red);')
    # color:#888 -> color:var(--red)
    slide_20_part = slide_20_part.replace('color:#888;', 'color:var(--red);')
    # color:var(--green) -> color:var(--red)
    slide_20_part = slide_20_part.replace('color:var(--green);', 'color:var(--red);')
    # background:var(--green) -> background:var(--red)
    slide_20_part = slide_20_part.replace('background:var(--green);', 'background:var(--red);')
    # color:var(--gold) -> color:var(--red)
    slide_20_part = slide_20_part.replace('color:var(--gold);', 'color:var(--red);')
    # border-left:3px solid var(--gold) -> border-left:3px solid var(--red)
    slide_20_part = slide_20_part.replace('border-left:3px solid var(--gold);', 'border-left:3px solid var(--red);')
    # border-left:3px solid var(--green) -> border-left:3px solid var(--red)
    slide_20_part = slide_20_part.replace('border-left:3px solid var(--green);', 'border-left:3px solid var(--red);')

    # text = text[:start_idx] + slide_20_part + text[end_idx:] # Don't update this yet, will do it below cleanly.
    text = text.replace(text[start_idx:end_idx], slide_20_part)

# 7. Button Colors for Slide 19 (which is Slide index 19 if 0-based... Wait, if my new slide makes 21 total slides,
# Slide 20 (Resultados) is index 19!
# User: "y los botones de anterior sigiente va en rojo."
# In JS:
'''
        if (cur === 0 || cur === 1) {
          ctrls.forEach(c => { c.style.color = 'var(--red)'; c.style.borderColor = 'rgba(232, 41, 68, 0.5)'; c.style.mixBlendMode = 'normal'; });
        } else if (isWhite) {
          const colors = ['var(--purple)', 'var(--red)', 'var(--gold)'];
          const clr = colors[cur % 3];
          ctrls.forEach(c => { c.style.color = clr; c.style.borderColor = clr; c.style.mixBlendMode = 'normal'; });
        } else {
          ctrls.forEach(c => { c.style.color = '#fff'; c.style.borderColor = 'rgba(255, 255, 255, 0.2)'; c.style.mixBlendMode = 'difference'; });
        }
'''
js_buttons_old = """
        if (cur === 0 || cur === 1) {
          ctrls.forEach(c => { c.style.color = 'var(--red)'; c.style.borderColor = 'rgba(232, 41, 68, 0.5)'; c.style.mixBlendMode = 'normal'; });
        } else if (isWhite) {
          const colors = ['var(--purple)', 'var(--red)', 'var(--gold)'];
          const clr = colors[cur % 3];
          ctrls.forEach(c => { c.style.color = clr; c.style.borderColor = clr; c.style.mixBlendMode = 'normal'; });
        } else {
          ctrls.forEach(c => { c.style.color = '#fff'; c.style.borderColor = 'rgba(255, 255, 255, 0.2)'; c.style.mixBlendMode = 'difference'; });
        }
"""
js_buttons_new = """
        if (cur === 0 || cur === 1 || cur === 19) {
          ctrls.forEach(c => { c.style.color = 'var(--red)'; c.style.borderColor = 'var(--red)'; c.style.mixBlendMode = 'normal'; c.style.background = 'transparent'; });
        } else if (isWhite) {
          const colors = ['var(--purple)', 'var(--red)', 'var(--gold)'];
          const clr = colors[cur % 3];
          ctrls.forEach(c => { c.style.color = clr; c.style.borderColor = clr; c.style.mixBlendMode = 'normal'; });
        } else {
          ctrls.forEach(c => { c.style.color = '#fff'; c.style.borderColor = 'rgba(255, 255, 255, 0.2)'; c.style.mixBlendMode = 'difference'; });
        }
"""
text = text.replace(js_buttons_old.strip(), js_buttons_new.strip())

# 8. Update PLACES array
places_old = """
      const PLACES = [
        [0, 10, 75, 50, 0, -15],  // slide 1 (0): opacity 0
        [1, -10, 75, 25, 1, 18],  // slide 2 (1): gatoazul
        [2, 25, 42, 12, 1, -8],   // slide 3 (2): aiñ
        [3, -5, 55, 25, 1, 22],   // slide 4 (3): gusanito
        [6, 5, 50, 12, 1, -20],   // slide 5 (4): ojito
        [5, 75, 80, 20, 1, 12],   // slide 6 (5)
        [6, -5, 85, 20, 0, -5],   // slide 7 (6) (ojito opacity 0)
        [7, 60, 5, 50, 0, 15],    // slide 8 (7): opacity 0
        [0, 40, 70, 64, 0, 30],   // slide 9 (8): opacity 0
        [2, 55, 60, 48, 0, -25],  // slide 10 (9): opacity 0
        [3, 5, 85, 22, 1, 10],    // slide 11 (10)
        [5, 75, -5, 25, 1, -15],  // slide 12 (11)
        [6, 5, 80, 20, 1, 25],    // slide 13 (12)
        [7, 75, 85, 12, 1, -12],  // slide 14 (13)
        [1, 15, 28, 12, 1, 15],   // slide 15 (14): gato corrido a la der
        [4, 10, 75, 15, 1, -30],  // slide 16 (15): huesito arriba a la derecha
        [0, 5, 85, 20, 1, 5],     // slide 17 (16)
        [3, 60, 80, 25, 1, -10],  // slide 18 (17)
        [8, 55, 80, 18, 1, -5],   // slide 19 (18): lengua.svg
        [0, 10, 75, 50, 0, 0]     // slide 20 (19): dummy
      ];
"""
places_new = """
      const PLACES = [
        [0, 10, 75, 50, 0, -15],  // slide 1 (0): opacity 0
        [1, -20, 80, 25, 1, 18],  // slide 2 (1): gatoazul moved up and right
        [2, 20, 42, 25, 1, -8],   // slide 3 (2): aiñ bigger
        [3, -5, 55, 25, 1, 22],   // slide 4 (3): gusanito
        [6, 5, 50, 12, 1, -20],   // slide 5 (4): ojito
        [5, 75, 80, 20, 1, 12],   // slide 6 (5)
        [6, -5, 85, 20, 0, -5],   // slide 7 (6) (ojito opacity 0)
        [0, -10, -10, 10, 0, 0],  // slide 8 (7): NEW QR SLIDE dummy
        [7, 60, 5, 50, 0, 15],    // slide 9 (8): Galeria 1 opacity 0
        [0, 40, 70, 64, 0, 30],   // slide 10 (9): Galeria 2 opacity 0
        [2, 55, 60, 48, 0, -25],  // slide 11 (10): Galeria 3 opacity 0
        [3, 5, 85, 22, 1, 10],    // slide 12 (11): Publico
        [5, 5, 45, 20, 1, 0],     // slide 13 (12): Web -> happy top center
        [6, 5, 80, 20, 1, 25],    // slide 14 (13): Revista 1
        [7, 75, 85, 12, 1, -12],  // slide 15 (14): Revista 2
        [1, 15, 28, 12, 1, 15],   // slide 16 (15): Empaque
        [4, 10, 75, 15, 1, -30],  // slide 17 (16): POP
        [0, 5, 85, 20, 1, 5],     // slide 18 (17): Estrategia
        [3, 60, 80, 25, 1, -10],  // slide 19 (18): Roles
        [8, 55, 80, 18, 1, -5],   // slide 20 (19): Resultados (lengua)
        [0, 10, 75, 50, 0, 0]     // slide 21 (20): Cierre
      ];
"""
text = text.replace(places_old.strip(), places_new.strip())

# Finally write
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)
print("Changes applied!")
