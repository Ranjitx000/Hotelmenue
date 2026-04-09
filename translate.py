import sys
import io

html = io.open(r'd:\freelance\index.html', 'r', encoding='utf-8').read()

replacements = [
    # 1. Truffle 
    ('''<h3 class="text-base tracking-tight font-medium text-zinc-100 leading-tight">Truffle Malai Kofta</h3>''',
     '''<h3 class="text-base tracking-tight font-medium text-zinc-100 leading-tight translatable" data-en="Truffle Malai Kofta" data-hi="ट्रफल मलाई कोफ्ता" data-mr="ट्रफल मलाई कोफ्ता">Truffle Malai Kofta</h3>'''),
    ('''Chef's Pick
                                </span>''',
     '''<span class="translatable" data-en="Chef's Pick" data-hi="शेफ की पसंद" data-mr="शेफची पसंती">Chef's Pick</span>
                                </span>'''),
    ('''<p class="text-xs text-zinc-400 line-clamp-2 leading-relaxed font-light mt-1">Hand-crafted paneer dumplings submerged in a rich cashew-saffron gravy, infused with black truffle oil.</p>''',
     '''<p class="text-xs text-zinc-400 line-clamp-2 leading-relaxed font-light mt-1 translatable" data-en="Hand-crafted paneer dumplings submerged in a rich cashew-saffron gravy, infused with black truffle oil." data-hi="काले ट्रफल तेल से युक्त काजू-केसर की गाढ़ी ग्रेवी में डूबे हाथ से बने पनीर के डंपलिंग।" data-mr="ब्लॅक ट्रफल तेलाच्या स्वादासह काजू-केशराच्या दाट ग्रेव्हीमध्ये बुडवलेले हाताने बनवलेले पनीर डंपलिंग.">Hand-crafted paneer dumplings submerged in a rich cashew-saffron gravy, infused with black truffle oil.</p>'''),

    # 2. Dal Makhani
    ('''<h3 class="text-base tracking-tight font-medium text-zinc-100 leading-tight">Smoked Dal Makhani</h3>''',
     '''<h3 class="text-base tracking-tight font-medium text-zinc-100 leading-tight translatable" data-en="Smoked Dal Makhani" data-hi="स्मोक्ड दाल मखनी" data-mr="स्मोक्ड दाल मखनी">Smoked Dal Makhani</h3>'''),
    ('''Classic
                                </span>''',
     '''<span class="translatable" data-en="Classic" data-hi="क्लासिक" data-mr="क्लासिक">Classic</span>
                                </span>'''),
    ('''<p class="text-xs text-zinc-400 line-clamp-2 leading-relaxed font-light mt-1">24-hour slow-cooked black lentils, enhanced with charcoal smoke, farm-fresh buttercream, and fenugreek.</p>''',
     '''<p class="text-xs text-zinc-400 line-clamp-2 leading-relaxed font-light mt-1 translatable" data-en="24-hour slow-cooked black lentils, enhanced with charcoal smoke, farm-fresh buttercream, and fenugreek." data-hi="24 घंटे धीमी आंच पर पकाई गई काली दाल, जिसे चारकोल के धुएं, ताज़े मक्खन और मेथी के साथ परोसी जाती है।" data-mr="24 तास मंद आचेवर शिजवलेली काळी डाळ, कोळशाच्या धुराने, ताजे लोणी आणि मेथीने सजवलेली.">24-hour slow-cooked black lentils, enhanced with charcoal smoke, farm-fresh buttercream, and fenugreek.</p>'''),

    # 3. Rasmalai
    ('''<h3 class="text-base tracking-tight font-medium text-zinc-100 leading-tight">Saffron Rasmalai Mille-Feuille</h3>''',
     '''<h3 class="text-base tracking-tight font-medium text-zinc-100 leading-tight translatable" data-en="Saffron Rasmalai Mille-Feuille" data-hi="केसर रसमलाई मिल-फील" data-mr="केशर रसमलाई मिल-फील">Saffron Rasmalai Mille-Feuille</h3>'''),
    ('''Dessert
                                </span>''',
     '''<span class="translatable" data-en="Dessert" data-hi="मिठाई" data-mr="गोड पदार्थ">Dessert</span>
                                </span>'''),
    ('''<p class="text-xs text-zinc-400 line-clamp-2 leading-relaxed font-light mt-1">Deconstructed rasmalai layered with crisp phyllo sheets, pistachio mousse, and 24k edible gold leaf.</p>''',
     '''<p class="text-xs text-zinc-400 line-clamp-2 leading-relaxed font-light mt-1 translatable" data-en="Deconstructed rasmalai layered with crisp phyllo sheets, pistachio mousse, and 24k edible gold leaf." data-hi="कुरकुरी फाइलो शीट्स, पिस्ता मूस और 24k खाद्य सोने के वर्क के साथ लेयर की गई डीकंस्ट्रक्टेड रसमलाई।" data-mr="कुरकुरीत फायलो शीट्स, पिस्ता मूस आणि 24k खाण्यायोग्य सोन्याच्या वर्खाने थर दिलेली डीकन्स्ट्रक्टेड रसमलाई.">Deconstructed rasmalai layered with crisp phyllo sheets, pistachio mousse, and 24k edible gold leaf.</p>'''),

    # 4. Nalli
    ('''<h3 class="text-base tracking-tight font-medium text-zinc-100 leading-tight">Nalli Nihari Osso Buco</h3>''',
     '''<h3 class="text-base tracking-tight font-medium text-zinc-100 leading-tight translatable" data-en="Nalli Nihari Osso Buco" data-hi="नल्ली निहारी ओस्सो बुको" data-mr="नल्ली निहारी ओसो बुको">Nalli Nihari Osso Buco</h3>'''),
    ('''Signature
                                </span>''',
     '''<span class="translatable" data-en="Signature" data-hi="सिग्नेचर" data-mr="सिग्नेचर">Signature</span>
                                </span>'''),
    ('''<p class="text-xs text-zinc-400 line-clamp-2 leading-relaxed font-light mt-1">Slow-braised lamb shank in deeply aromatic royal Awadhi spices, finished with rose water and vetiver.</p>''',
     '''<p class="text-xs text-zinc-400 line-clamp-2 leading-relaxed font-light mt-1 translatable" data-en="Slow-braised lamb shank in deeply aromatic royal Awadhi spices, finished with rose water and vetiver." data-hi="गुलाब जल और खस के साथ समाप्त हुए शाही अवधी मसालों में धीमी आंच पर पका मेमने का शैंक।" data-mr="गुलाब पाणी आणि खसच्या स्वादासह अत्यंत सुगंधी शाही अवधी मसाल्यांमध्ये मंद आचेवर शिजवलेले मटण शँक.">Slow-braised lamb shank in deeply aromatic royal Awadhi spices, finished with rose water and vetiver.</p>'''),

    # 5. Chicken
    ('''<h3 class="text-base tracking-tight font-medium text-zinc-100 leading-tight">Chicken Tikka Cannelloni</h3>''',
     '''<h3 class="text-base tracking-tight font-medium text-zinc-100 leading-tight translatable" data-en="Chicken Tikka Cannelloni" data-hi="चिकन टिक्का कैनेलोनी" data-mr="चिकन टिक्का कॅनेलोनी">Chicken Tikka Cannelloni</h3>'''),
    ('''Fusion
                                </span>''',
     '''<span class="translatable" data-en="Fusion" data-hi="फ्यूजन" data-mr="फ्युजन">Fusion</span>
                                </span>'''),
    ('''<p class="text-xs text-zinc-400 line-clamp-2 leading-relaxed font-light">Charcoaled tandoori chicken encased in artisanal pasta sheets, topped with makhani foam and micro-cilantro.</p>''',
     '''<p class="text-xs text-zinc-400 line-clamp-2 leading-relaxed font-light translatable" data-en="Charcoaled tandoori chicken encased in artisanal pasta sheets, topped with makhani foam and micro-cilantro." data-hi="मखनी फोम और माइक्रो-धनिया के साथ आर्टिसनल पास्ता शीट्स में लिपटा चारकोल तंदूरी चिकन।" data-mr="मखनी फोम आणि मायक्रो-कोथिंबीरने सजवलेले आर्टिसनल पास्ता शीट्समध्ये गुंडाळलेले चारकोल तंदूरी चिकन.">Charcoaled tandoori chicken encased in artisanal pasta sheets, topped with makhani foam and micro-cilantro.</p>'''),

    # 6. Lobster
    ('''<h3 class="text-base tracking-tight font-medium text-zinc-100 leading-tight">Tandoori Lobster Tail</h3>''',
     '''<h3 class="text-base tracking-tight font-medium text-zinc-100 leading-tight translatable" data-en="Tandoori Lobster Tail" data-hi="तंदूरी लॉबस्टर टेल" data-mr="तंदूरी लॉबस्टर टेल">Tandoori Lobster Tail</h3>'''),
    ('''<p class="text-xs text-zinc-400 line-clamp-2 leading-relaxed font-light mt-1">Clay oven roasted Atlantic lobster, marinated in Kashmiri chili and hung curd, served with coconut moilee sauce.</p>''',
     '''<p class="text-xs text-zinc-400 line-clamp-2 leading-relaxed font-light mt-1 translatable" data-en="Clay oven roasted Atlantic lobster, marinated in Kashmiri chili and hung curd, served with coconut moilee sauce." data-hi="कश्मीरी मिर्च और हंग कर्ड में मैरिनेट किया हुआ ओवन रोस्टेड अटलांटिक लॉबस्टर, जिसे नारियल मोइली सॉस के साथ परोसा जाता है।" data-mr="काश्मिरी मिरची आणि घट्ट दह्यात मॅरीनेट केलेले ओव्हन रोस्टेड अटलांटिक लॉबस्टर, कोकोनट मोइली सॉससोबत.">Clay oven roasted Atlantic lobster, marinated in Kashmiri chili and hung curd, served with coconut moilee sauce.</p>'''),

    # 7. Gobi
    ('''<h3 class="text-base tracking-tight font-medium text-zinc-100 leading-tight">Tandoori Gobi Musallam</h3>''',
     '''<h3 class="text-base tracking-tight font-medium text-zinc-100 leading-tight translatable" data-en="Tandoori Gobi Musallam" data-hi="तंदूरी गोभी मुसल्लम" data-mr="तंदूरी गोबी मुसल्लम">Tandoori Gobi Musallam</h3>'''),
    ('''Plant-Based
                                </span>''',
     '''<span class="translatable" data-en="Plant-Based" data-hi="प्लांट-बेस्ड" data-mr="प्लांट-बेस्ड">Plant-Based</span>
                                </span>'''),
    ('''<p class="text-xs text-zinc-400 line-clamp-2 leading-relaxed font-light mt-1">Whole roasted cauliflower basted in a rich almond and coconut gravy, topped with caramelized onions.</p>''',
     '''<p class="text-xs text-zinc-400 line-clamp-2 leading-relaxed font-light mt-1 translatable" data-en="Whole roasted cauliflower basted in a rich almond and coconut gravy, topped with caramelized onions." data-hi="बादाम और नारियल की ग्रेवी में पकी और कैरामेलाइज़्ड प्याज़ से सजी साबुत भुनी हुई गोभी।" data-mr="बदाम आणि नारळाच्या ग्रेव्हीमध्ये शिजवलेली आणि कॅरमेलाईज्ड कांद्याने सजवलेली अख्खी भाजलेली फ्लॉवर.">Whole roasted cauliflower basted in a rich almond and coconut gravy, topped with caramelized onions.</p>'''),
    
    # 8. Cardamom
    ('''<h3 class="text-base tracking-tight font-medium text-zinc-100 leading-tight">Cardamom Old Fashioned</h3>''',
     '''<h3 class="text-base tracking-tight font-medium text-zinc-100 leading-tight translatable" data-en="Cardamom Old Fashioned" data-hi="इलायची ओल्ड फैशंड" data-mr="वेलची ओल्ड फॅशंड">Cardamom Old Fashioned</h3>'''),
    ('''<p class="text-xs text-zinc-400 line-clamp-2 leading-relaxed font-light mt-1">Single malt whiskey stirred with cardamom-infused jaggery syrup, finished with aromatic smoke.</p>''',
     '''<p class="text-xs text-zinc-400 line-clamp-2 leading-relaxed font-light mt-1 translatable" data-en="Single malt whiskey stirred with cardamom-infused jaggery syrup, finished with aromatic smoke." data-hi="इलायची वाले गुड़ के सिरप के साथ सिंगल माल्ट व्हिस्की, और धुएं की सुगंध।" data-mr="वेलची आणि गुळाच्या सिरपमध्ये मिसळलेली सिंगल माल्ट व्हिस्की, आणि सुगंधी धूर.">Single malt whiskey stirred with cardamom-infused jaggery syrup, finished with aromatic smoke.</p>'''),

    # 9. Kala Khata
    ('''<h3 class="text-base tracking-tight font-medium text-zinc-100 leading-tight">Kala Khatta Cooler</h3>''',
     '''<h3 class="text-base tracking-tight font-medium text-zinc-100 leading-tight translatable" data-en="Kala Khatta Cooler" data-hi="काला खट्टा कूलर" data-mr="काला खट्टा कूलर">Kala Khatta Cooler</h3>'''),
    ('''<p class="text-xs text-zinc-400 line-clamp-2 leading-relaxed font-light mt-1">Jamun fruit extract, black salt, fresh lime, and sparkling water with a chili-salt rim. (Non-Alcoholic)</p>''',
     '''<p class="text-xs text-zinc-400 line-clamp-2 leading-relaxed font-light mt-1 translatable" data-en="Jamun fruit extract, black salt, fresh lime, and sparkling water with a chili-salt rim. (Non-Alcoholic)" data-hi="जामुन का रस, काला नमक, ताज़ा नींबू और स्पार्कलिंग पानी, मिर्च-नमक लगे किनारे के साथ।" data-mr="जांभळाचा अर्क, काळे मीठ, ताजे लिंबू आणि स्पार्कलिंग पाणी, मिरची-मीठ लावलेल्या कडांसह.">Jamun fruit extract, black salt, fresh lime, and sparkling water with a chili-salt rim. (Non-Alcoholic)</p>''')
]

for old, new_text in replacements:
    if old in html:
        html = html.replace(old, new_text)
    else:
        print('FAILED TO FIND:', old.strip()[:30])

io.open(r'd:\freelance\index.html', 'w', encoding='utf-8').write(html)
