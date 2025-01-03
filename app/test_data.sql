insert into hotels (name, location, services, rooms_quntity, image_id) values
('Astra', 'Центральная, 127, с. Анос, Чемальский район, Республика Алтай', '["Wi-Fi", "Парковка", "Тренажёрный зал", "Кондиционе"]', 20, 1),
('Bistro', 'Приозёрный проезд, 1Б, с. Озерное, Майминский район, Республика Алтай', '["Wi-Fi", "Парковка"]', 22, 2),
('Kosmo', 'Улица Центральная, 53, с. Соузга, Майминский район, Республика Алтай', '["Wi-Fi", "Тренажёрный зал", "Кондиционе"]', 18, 3),
('Turist', 'Чемальский тракт 15 км, 14 к1, с. Чепош, Чемальский район, Республика Алтай', '["Wi-Fi", "Кондиционе"]', 25, 4),
('Altai', 'Приозёрный проезд, 11, с. Озерное, Майминский район, Республика Алтай', '["Тренажёрный зал", "Кондиционе"]', 21, 5),
('Svoboda', 'Манжерок, микрорайон Курорт Манжерок, 1, с. Озерное, Майминский район, Республика', '["Парковка", "Тренажёрный зал", "Кондиционе"]', 38, 6);


insert into rooms (hotel_id, name, price,quantity, services,  image_id) values
(1, 'С видом на озеро', 20400, 5, '["Бесплатный Wi-Fi", "Кондиционер", "Холодильник"]', 7),
(1, 'С видом на поле', 21400, 15, '["Кондиционер", "Холодильник"]', 8),
(2, 'С видом на горы', 24300, 2, '[]', 9),
(3, 'С видом на лес', 21200, 1, '["Бесплатный Wi-Fi", "Холодильник"]', 10),
(3, 'С видом на животных', 7400, 8, '["Бесплатный Wi-Fi", "Кондиционер"]', 11),
(4, 'С видом на рыб', 26500, 15, '["Холодильник"]', 12),
(5, 'С видом на город', 16400, 14, '["Бесплатный Wi-Fi"]', 13),
(5, 'С видом на людей', 38400, 13, '["Кондиционер"]', 14),
(6, 'С видом на счастье', 10400, 8, '["Бесплатный Wi-Fi", "Кондиционер"]', 15);


insert into users (email, hashed_password) values
('fsdsd@mail.com', 'HP_1'),
('gdfgdf@mail.ru', 'HP_2'),
('rwe4ret@gmail.com', 'HP_3'),
('gdfgd@mail.com', 'HP_4'),
('dgfrjk@gmail.com', 'HP_5'),
('sdfse4@yandex.ru', 'HP_6');

insert into bookings (room_id, user_id, date_from, date_to, price) values
(1, 3, '2024-12-11', '2024-12-12', 24300),
(4, 5, '2024-11-10', '2024-11-14', 21200),
(2, 1, '2024-12-14', '2024-12-21', 21400),
(5, 2, '2024-10-17', '2024-12-11', 7400),
(5, 5, '2024-12-21', '2024-12-25', 7400),
(3, 6, '2024-09-21', '2024-09-30', 26500);

