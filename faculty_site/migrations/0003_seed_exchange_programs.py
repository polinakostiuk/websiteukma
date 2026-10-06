from django.db import migrations

SQL_FORWARD = """
INSERT INTO faculty_site_exchangeprogram (university, languages, places, deadline, description)
VALUES
('Uniwersytet Warszawski, Польща', 'польська, англійська', '5', '2026-11-15', 'Один із найстаріших та найбільших університетів Польщі з багатим вибором гуманітарних дисциплін.'),
('KU Leuven (Бельгія)', 'English', '2 місяці', '2026-12-01', 'Провідний європейський дослідницький університет із потужними англомовними програмами.'),
('Vilnius University, Литва', 'англійська', 'до 4', '2026-10-20', 'Класичний балтійський університет із дружньою до українських студентів академічною спільнотою.'),
('Uniwersytet Jagielloński, Польща', 'Польська, Англійська', '3', '2026-11-15', 'Найстаріший виш Польщі з визнаними філологічними та історичними школами.'),
('University of Tartu - Естонія', 'англійська, естонська', '2', '2027-01-10', 'Провідний університет Естонії з високими стандартами цифровізації навчання.'),
('Masaryk University, Чехія', 'англійська', '1 місце', '2026-09-30', 'Сучасний виш Чехії, розташований у студентському місті Брно.');
"""
SQL_REVERSE = """
DELETE FROM faculty_site_exchangeprogram
WHERE university IN (
    'Uniwersytet Warszawski, Польща',
    'KU Leuven (Бельгія)',
    'Vilnius University, Литва',
    'Uniwersytet Jagielloński, Польща',
    'University of Tartu - Естонія',
    'Masaryk University, Чехія'
);
"""

class Migration(migrations.Migration):

    dependencies = [
        ('faculty_site', '0002_add_exchange_program_model'),
    ]

    operations = [
        migrations.RunSQL(SQL_FORWARD, reverse_sql=SQL_REVERSE),
    ]
