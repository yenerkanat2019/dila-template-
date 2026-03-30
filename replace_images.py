import glob, re

# Map files to images
updates = {
    'template-03.html': [
        (r'\.ems-img\s*\{[^}]*background:\s*#f0f0f0;[^}]*\}', ".ems-img { height: 600px; background: url('assets/img/ems_machine.png') center/cover; border-radius: 8px; position: relative; z-index: 2; }"),
        (r'>İmaj Alanı<', "><")
    ],
    'template-04.html': [
        (r'\.img-placeholder\s*\{[^}]*\}', ".img-placeholder { background: url('assets/img/machine_1.jpg') center/cover; border-radius: 20px; height: 100%; min-height: 200px; position: relative; }"),
        (r'\.img-placeholder::after\s*\{[^}]*\}', "") # Remove text overlay
    ],
    'template-05.html': [
        (r'\.img-frame\s*\{[^}]*\}', ".img-frame { width: 100%; height: 100%; border-radius: 200px 200px 20px 20px; background: url('assets/img/spa_1.jpg') center/cover; position: relative; z-index: 2; box-shadow: 0 30px 60px rgba(0,0,0,0.06); }"),
        (r'\.img-frame::before\s*\{[^}]*\}', ""),
        (r'\.overlap-img\s*\{[^}]*\}', ".overlap-img { height: 600px; background: url('assets/img/fitness_1.jpg') center/cover; position: relative; }"),
        (r'>B-8317 Cihaz & Estetik Görsel<', "><")
    ],
    'template-06.html': [
        (r'\.glass-panel\s*\{[^}]*\}', ".glass-panel { width: 100%; height: 100%; background: url('assets/img/ems_machine.png') center/cover; border-radius: 20px; transform: rotateY(-5deg) rotateX(5deg); box-shadow: -20px 20px 50px rgba(0,0,0,0.5); transition: 0.5s; }"),
        (r'\.glass-panel::before\s*\{[^}]*\}', "")
    ],
    'template-07.html': [
        (r'\.arch-frame\s*\{[^}]*\}', ".arch-frame { width: 90%; height: 95%; background: url('assets/img/measure_1.jpg') center/cover; border-radius: 999px 999px 0 0; position: relative; box-shadow: 0 40px 100px rgba(26,40,31,0.06); animation: arch-breathe 8s ease-in-out infinite alternate; }"),
        (r'\.art-img\s*\{[^}]*\}', ".art-img { width: 100%; height: 600px; background: url('assets/img/healthy_diet.png') center/cover; border-radius: 0 200px 0 200px; position: relative; }"),
        (r'>Huzur ve Sağlık<', "><"),
        (r'>Denge\.<', "><")
    ],
    'template-08.html': [
        (r'\.hero-img\s*\{[^}]*\}', ".hero-img { width: 100%; max-width: 1200px; height: 500px; background: url('assets/img/clinic_1.jpg') center/cover; border-radius: 40px 40px 0 0; margin-top: auto; }"),
        (r'\.split-img\s*\{[^}]*\}', ".split-img { flex: 1; height: 600px; background: url('assets/img/fit_client.png') center/cover; border-radius: 20px; }"),
        (r'>Zarif Klinik veya Cihaz Görseli<', "><")
    ],
    'template-09.html': [
        (r'\.tech-visual\s*\{[^}]*\}', ".tech-visual { flex: 1; position: relative; background: url('assets/img/spa_2.jpg') center/cover; }"),
        (r'\.tech-visual::before\s*\{[^}]*\}', "")
    ],
    'template-10.html': [
        (r'\.cp-img-in\s*\{[^}]*\}', ".cp-img-in { width: 100%; height: 100%; border: 4px solid #fff; border-radius: 50%; background: url('assets/img/doctor_1.jpg') center/cover; }"),
        (r'\.vp-img\s*\{[^}]*\}', ".vp-img { height: 200px; background-size: cover; background-position: center; display: flex; align-items: center; justify-content: center; font-size: 32px; color: #fff; font-weight: 900; box-shadow: inset 0 0 0 1000px rgba(0,0,0,0.3); }"),
        (r'style="background:var\(--blue\)"', 'style="background-image: url(\'assets/img/diet_2.jpg\');"'),
        (r'style="background:var\(--ig-p\)"', 'style="background-image: url(\'assets/img/fitness_1.jpg\');"'),
        (r'style="background:var\(--text\)"', 'style="background-image: url(\'assets/img/spa_1.jpg\');"')
    ]
}

for file, rules in updates.items():
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        for pattern, replacement in rules:
            content = re.sub(pattern, replacement, content)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
    except Exception as e:
        print(f"Failed {file}: {e}")
