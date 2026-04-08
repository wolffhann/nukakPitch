$path = "c:\Users\user\Downloads\Pitch\Pitch\pitch.html"
$content = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)

# 1. Update Index
$content = $content.Replace('08</div>' + "`n" + '              <div style="padding-top:0.25rem;">' + "`n" + '                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Galería Visual', '09</div>' + "`n" + '              <div style="padding-top:0.25rem;">' + "`n" + '                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Galería Visual')
$content = $content.Replace('11</div>' + "`n" + '              <div style="padding-top:0.25rem;">' + "`n" + '                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Público Objetivo', '12</div>' + "`n" + '              <div style="padding-top:0.25rem;">' + "`n" + '                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Público Objetivo')
$content = $content.Replace('12</div>' + "`n" + '              <div style="padding-top:0.25rem;">' + "`n" + '                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Ecosistema Web', '13</div>' + "`n" + '              <div style="padding-top:0.25rem;">' + "`n" + '                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Ecosistema Web')
$content = $content.Replace('15</div>' + "`n" + '              <div style="padding-top:0.25rem;">' + "`n" + '                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Empaque 3D', '16</div>' + "`n" + '              <div style="padding-top:0.25rem;">' + "`n" + '                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Empaque 3D')
$content = $content.Replace('16</div>' + "`n" + '              <div style="padding-top:0.25rem;">' + "`n" + '                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Material POP', '17</div>' + "`n" + '              <div style="padding-top:0.25rem;">' + "`n" + '                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Material POP')
$content = $content.Replace('17</div>' + "`n" + '              <div style="padding-top:0.25rem;">' + "`n" + '                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Estrategia', '18</div>' + "`n" + '              <div style="padding-top:0.25rem;">' + "`n" + '                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Estrategia')
$content = $content.Replace('18</div>' + "`n" + '              <div style="padding-top:0.25rem;">' + "`n" + '                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Roles', '19</div>' + "`n" + '              <div style="padding-top:0.25rem;">' + "`n" + '                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Roles')
$content = $content.Replace('19</div>' + "`n" + '              <div style="padding-top:0.25rem;">' + "`n" + '                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Resultados', '20</div>' + "`n" + '              <div style="padding-top:0.25rem;">' + "`n" + '                <div style="font-weight:800;font-size:.9vw;text-transform:uppercase;">Resultados')

# 2. Add New Slide 8
$newSlide = '    <!-- ══ SLIDE NUEVA: QR MANUAL DE MARCA ══ -->' + "`n" + '    <section class="slide tc center-slide" style="background:var(--purple); padding:0;">' + "`n" + '      <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; gap:2.5rem; width:100%;">' + "`n" + '        <h2 style="font-size:4.5vw; color:#fff; text-align:center; font-family:''Montserrat''; font-weight:900;">Escanea para ver el<br>Manual de Marca NUKAK.</h2>' + "`n" + '        <div style="width:40vh; height:40vh; background:#fff; padding:1.5rem; border-radius:16px; box-shadow:0 15px 35px rgba(0,0,0,0.3);">' + "`n" + '          <img src="foticx/QR manual nukak.png" style="width:100%; height:100%; object-fit:contain;">' + "`n" + '        </div>' + "`n" + '      </div>' + "`n" + '    </section>' + "`n`n" + '    <!-- ══ SLIDE 08: GALERÍA 1 ══ -->'
$content = $content.Replace('    <!-- ══ SLIDE 08: GALERÍA 1 ══ -->', $newSlide)

# 3. Slide 8 (now 9), 9 (now 10), 10 (now 11) styles
# We just use precise replaces. We extract padding and change img tag.
$gal1old = 'style="padding: 0 2vw; position:relative;">' + "`n" + '      <img src="foticx/logo.svg" style="width:100%; height:94vh; object-fit:contain; z-index:1;">'
$gal1new = 'style="padding: 0; position:relative;">' + "`n" + '      <img src="foticx/logo.svg" style="width:100%; height:100vh; object-fit:cover; z-index:1;">'
$content = $content.Replace($gal1old, $gal1new)

$gal2old = 'style="padding: 0 2vw;">' + "`n" + '      <img src="foticx/paleta.svg" style="width:100%; height:94vh; object-fit:contain;">'
$gal2new = 'style="padding: 0;">' + "`n" + '      <img src="foticx/paleta.svg" style="width:100%; height:100vh; object-fit:cover;">'
$content = $content.Replace($gal2old, $gal2new)

$gal3old = 'style="padding: 0 2vw;">' + "`n" + '      <img src="foticx/tipografia.svg" style="width:100%; height:94vh; object-fit:contain;">'
$gal3new = 'style="padding: 0;">' + "`n" + '      <img src="foticx/tipografia.svg" style="width:100%; height:100vh; object-fit:cover;">'
$content = $content.Replace($gal3old, $gal3new)

# QR Box
$qrBox = '      <div' + "`n" + '        style="position:absolute; bottom:5vh; right:5vw; z-index:10; display:flex; flex-direction:row; align-items:center; gap:1rem; background:rgba(0,0,0,0.5); padding:1rem; border-radius:12px; backdrop-filter:blur(5px); border:1px solid rgba(255,255,255,0.1); box-shadow:0 10px 30px rgba(0,0,0,0.5);">' + "`n" + '        <p' + "`n" + '          style="font-family:''Montserrat''; font-size:1vw; font-weight:800; color:#fff; text-transform:uppercase; text-align:right; line-height:1.2; max-width:160px;">' + "`n" + '          Escanea para ver el<br><span style="color:var(--green)">Manual de Marca<br>NUKAK</span></p>' + "`n" + '        <div style="width:100px; height:100px; background:#fff; padding:0.4rem; border-radius:8px;">' + "`n" + '          <img src="foticx/QR manual nukak.png" style="width:100%; height:100%; object-fit:contain;">' + "`n" + '        </div>' + "`n" + '      </div>'
$content = $content.Replace($qrBox, '')

# 4. Update the Ghost Tags and Tags numbers (Slide 19 -> 20, 18 -> 19... 08 -> 09)
for ($i = 19; $i -ge 8; $i--) {
    $old = "{0:D2}" -f $i
    $new = "{0:D2}" -f ($i+1)
    $content = $content.Replace(('<!-- ══ SLIDE ' + $old + ':'), ('<!-- ══ SLIDE ' + $new + ':'))
    $content = $content.Replace(('<div class="ghost" style="color:rgba(0,0,0,.04);">' + $old + '</div>'), ('<div class="ghost" style="color:rgba(0,0,0,.04);">' + $new + '</div>'))
    $content = $content.Replace(('<div class="ghost" style="color:rgba(0,0,0,.03);">' + $old + '</div>'), ('<div class="ghost" style="color:rgba(0,0,0,.03);">' + $new + '</div>'))
    $content = $content.Replace(('<div class="ghost ghost-w">' + $old + '</div>'), ('<div class="ghost ghost-w">' + $new + '</div>'))
    $content = $content.Replace(('<span class="tag rv d1">' + $old + ' —'), ('<span class="tag rv d1">' + $new + ' —'))
    $content = $content.Replace(('<span class="tag tag-w rv d1">' + $old + ' —'), ('<span class="tag tag-w rv d1">' + $new + ' —'))
}

# 5. Fix diapositiva 5 (mujernukak)
$content = $content.Replace('right:7vw; width:45vw; max-height:85vh;', 'right:2vw; width:55vw; max-height:95vh;')

# 6. Change Slide 19 (Old 19, new 20 -> Resultados)
$startIdx = $content.IndexOf('<!-- ══ SLIDE 20: RESULTADOS')
$endIdx = $content.IndexOf('<!-- ══ SLIDE 21')
if ($startIdx -ne -1 -and $endIdx -ne -1) {
    $slide20 = $content.Substring($startIdx, $endIdx - $startIdx)
    $slide20 = $slide20.Replace('color:#fff;', 'color:#000;')
    $slide20 = $slide20.Replace('color:#aaa;', 'color:var(--red);')
    $slide20 = $slide20.Replace('color:#888;', 'color:var(--red);')
    $slide20 = $slide20.Replace('color:var(--green);', 'color:var(--red);')
    $slide20 = $slide20.Replace('background:var(--green);', 'background:var(--red);')
    $slide20 = $slide20.Replace('color:var(--gold);', 'color:var(--red);')
    $slide20 = $slide20.Replace('border-left:3px solid var(--gold);', 'border-left:3px solid var(--red);')
    $slide20 = $slide20.Replace('border-left:3px solid var(--green);', 'border-left:3px solid var(--red);')
    
    $content = $content.Substring(0, $startIdx) + $slide20 + $content.Substring($endIdx)
}

# 7. Button Colors for Slide 19
$jsButtonsOld = '        if (cur === 0 || cur === 1) {' + "`n" + '          ctrls.forEach(c => { c.style.color = ''var(--red)''; c.style.borderColor = ''rgba(232, 41, 68, 0.5)''; c.style.mixBlendMode = ''normal''; });' + "`n" + '        } else if (isWhite) {' + "`n" + '          const colors = [''var(--purple)'', ''var(--red)'', ''var(--gold)''];' + "`n" + '          const clr = colors[cur % 3];' + "`n" + '          ctrls.forEach(c => { c.style.color = clr; c.style.borderColor = clr; c.style.mixBlendMode = ''normal''; });' + "`n" + '        } else {' + "`n" + '          ctrls.forEach(c => { c.style.color = ''#fff''; c.style.borderColor = ''rgba(255, 255, 255, 0.2)''; c.style.mixBlendMode = ''difference''; });' + "`n" + '        }'
$jsButtonsNew = '        if (cur === 0 || cur === 1 || cur === 19) {' + "`n" + '          ctrls.forEach(c => { c.style.color = ''var(--red)''; c.style.borderColor = ''var(--red)''; c.style.mixBlendMode = ''normal''; c.style.background = ''transparent''; });' + "`n" + '        } else if (isWhite) {' + "`n" + '          const colors = [''var(--purple)'', ''var(--red)'', ''var(--gold)''];' + "`n" + '          const clr = colors[cur % 3];' + "`n" + '          ctrls.forEach(c => { c.style.color = clr; c.style.borderColor = clr; c.style.mixBlendMode = ''normal''; });' + "`n" + '        } else {' + "`n" + '          ctrls.forEach(c => { c.style.color = ''#fff''; c.style.borderColor = ''rgba(255, 255, 255, 0.2)''; c.style.mixBlendMode = ''difference''; });' + "`n" + '        }'
$content = $content.Replace($jsButtonsOld, $jsButtonsNew)

# 8. Update PLACES array
$placesOld = '      const PLACES = [' + "`n" + '        [0, 10, 75, 50, 0, -15],  // slide 1 (0): opacity 0' + "`n" + '        [1, -10, 75, 25, 1, 18],  // slide 2 (1): gatoazul' + "`n" + '        [2, 25, 42, 12, 1, -8],   // slide 3 (2): aiñ' + "`n" + '        [3, -5, 55, 25, 1, 22],   // slide 4 (3): gusanito' + "`n" + '        [6, 5, 50, 12, 1, -20],   // slide 5 (4): ojito' + "`n" + '        [5, 75, 80, 20, 1, 12],   // slide 6 (5)' + "`n" + '        [6, -5, 85, 20, 0, -5],   // slide 7 (6) (ojito opacity 0)' + "`n" + '        [7, 60, 5, 50, 0, 15],    // slide 8 (7): opacity 0' + "`n" + '        [0, 40, 70, 64, 0, 30],   // slide 9 (8): opacity 0' + "`n" + '        [2, 55, 60, 48, 0, -25],  // slide 10 (9): opacity 0' + "`n" + '        [3, 5, 85, 22, 1, 10],    // slide 11 (10)' + "`n" + '        [5, 75, -5, 25, 1, -15],  // slide 12 (11)' + "`n" + '        [6, 5, 80, 20, 1, 25],    // slide 13 (12)' + "`n" + '        [7, 75, 85, 12, 1, -12],  // slide 14 (13)' + "`n" + '        [1, 15, 28, 12, 1, 15],   // slide 15 (14): gato corrido a la der' + "`n" + '        [4, 10, 75, 15, 1, -30],  // slide 16 (15): huesito arriba a la derecha' + "`n" + '        [0, 5, 85, 20, 1, 5],     // slide 17 (16)' + "`n" + '        [3, 60, 80, 25, 1, -10],  // slide 18 (17)' + "`n" + '        [8, 55, 80, 18, 1, -5],   // slide 19 (18): lengua.svg' + "`n" + '        [0, 10, 75, 50, 0, 0]     // slide 20 (19): dummy' + "`n" + '      ];'
$placesNew = '      const PLACES = [' + "`n" + '        [0, 10, 75, 50, 0, -15],  // slide 1 (0): opacity 0' + "`n" + '        [1, -20, 80, 25, 1, 18],  // slide 2 (1): gatoazul moved up and right' + "`n" + '        [2, 20, 42, 25, 1, -8],   // slide 3 (2): aiñ bigger' + "`n" + '        [3, -5, 55, 25, 1, 22],   // slide 4 (3): gusanito' + "`n" + '        [6, 5, 50, 12, 1, -20],   // slide 5 (4): ojito' + "`n" + '        [5, 75, 80, 20, 1, 12],   // slide 6 (5)' + "`n" + '        [6, -5, 85, 20, 0, -5],   // slide 7 (6) (ojito opacity 0)' + "`n" + '        [0, -10, -10, 10, 0, 0],  // slide 8 (7): NEW QR SLIDE dummy' + "`n" + '        [7, 60, 5, 50, 0, 15],    // slide 9 (8): Galeria 1 opacity 0' + "`n" + '        [0, 40, 70, 64, 0, 30],   // slide 10 (9): Galeria 2 opacity 0' + "`n" + '        [2, 55, 60, 48, 0, -25],  // slide 11 (10): Galeria 3 opacity 0' + "`n" + '        [3, 5, 85, 22, 1, 10],    // slide 12 (11): Publico' + "`n" + '        [5, 5, 45, 20, 1, 0],     // slide 13 (12): Web -> happy top center' + "`n" + '        [6, 5, 80, 20, 1, 25],    // slide 14 (13): Revista 1' + "`n" + '        [7, 75, 85, 12, 1, -12],  // slide 15 (14): Revista 2' + "`n" + '        [1, 15, 28, 12, 1, 15],   // slide 16 (15): Empaque' + "`n" + '        [4, 10, 75, 15, 1, -30],  // slide 17 (16): POP' + "`n" + '        [0, 5, 85, 20, 1, 5],     // slide 18 (17): Estrategia' + "`n" + '        [3, 60, 80, 25, 1, -10],  // slide 19 (18): Roles' + "`n" + '        [8, 55, 80, 18, 1, -5],   // slide 20 (19): Resultados (lengua)' + "`n" + '        [0, 10, 75, 50, 0, 0]     // slide 21 (20): Cierre' + "`n" + '      ];'
$content = $content.Replace($placesOld, $placesNew)

# Print lines added to verify
Write-Host "Success replacing text."

[System.IO.File]::WriteAllText($path, $content, [System.Text.Encoding]::UTF8)
