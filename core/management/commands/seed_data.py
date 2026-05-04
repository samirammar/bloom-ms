from django.core.management.base import BaseCommand
from core.models import SiteSettings
from projects.models import Project, ProjectCategory, Testimonial
from services.models import Service, ServiceCategory
from jobs.models import JobPosting
from django.utils.text import slugify
from django.conf import settings

class Command(BaseCommand):
    help = 'Seeds the database with initial professional data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # 1. Site Settings
        settings_obj, created = SiteSettings.objects.get_or_create(pk=1)
        settings_obj.email = 'hello@bloomstudio.com'
        settings_obj.phone = '+971 50 123 4567'
        settings_obj.address = 'Dubai Design District, Building 4, Dubai, UAE'
        
        # Set English translations
        settings_obj.set_current_language('en')
        settings_obj.company_name = 'Bloom Digital Studio'
        settings_obj.description = 'A premium digital studio specializing in high-performance web applications, mobile experiences, and microservices architecture.'
        settings_obj.tagline = 'Premium Digital Solutions'
        settings_obj.hero_title = 'Building Digital Excellence'
        settings_obj.hero_subtitle = 'We craft cutting-edge software solutions and microservices that transform your business into a digital powerhouse.'
        settings_obj.hero_cta_text = 'Start Your Project'
        settings_obj.hero_cta_link = '/en/contact/'
        settings_obj.about_title = 'About Bloom Digital'
        settings_obj.about_content = 'Founded in 2020, Bloom Digital Studio has been at the forefront of digital transformation. Our team of visionaries and engineers works tirelessly to deliver products that set new industry standards.'
        settings_obj.cta_title = 'Ready to Transform Your Business?'
        settings_obj.cta_content = "Let's discuss your project and build something amazing together."
        settings_obj.cta_button = 'Get a Quote'
        settings_obj.working_hours = 'Sunday - Thursday: 9:00 AM - 6:00 PM'
        
        # Set Arabic translations
        settings_obj.set_current_language('ar')
        settings_obj.company_name = 'استوديو بلوم الرقمي'
        settings_obj.description = 'استوديو رقمي متميز متخصص في تطبيقات الويب عالية الأداء وتجارب الهاتف المحمول وهندسة الخدمات المصغرة.'
        settings_obj.tagline = 'حلول رقمية مميزة'
        settings_obj.hero_title = 'بناء التميز الرقمي'
        settings_obj.hero_subtitle = 'نصنع حلول برمجية متطورة وخدمات مصغرة تحول عملك إلى قوة رقمية.'
        settings_obj.hero_cta_text = 'ابدأ مشروعك'
        settings_obj.hero_cta_link = '/ar/contact/'
        settings_obj.about_title = 'عن بلوم ديجيتال'
        settings_obj.about_content = 'تأسس استوديو بلوم الرقمي في عام 2020 وقد كان في طليعة التحول الرقمي.'
        settings_obj.cta_title = 'هل أنت مستعد لتحويل عملك؟'
        settings_obj.cta_content = 'دعنا نناقش مشروعك ونبني شيئًا رائعًا معًا.'
        settings_obj.cta_button = 'احصل على عرض سعر'
        settings_obj.working_hours = 'الأحد - الخميس: 9:00 صباحًا - 6:00 مساءً'
        
        settings_obj.save()
        self.stdout.write(self.style.SUCCESS('Site Settings seeded.'))

        # 2. Service Categories
        web_cat, _ = ServiceCategory.objects.get_or_create(slug='development')
        web_cat.set_current_language('en')
        web_cat.name = 'Development'
        web_cat.set_current_language('ar')
        web_cat.name = 'تطوير'
        web_cat.save()

        design_cat, _ = ServiceCategory.objects.get_or_create(slug='design')
        design_cat.set_current_language('en')
        design_cat.name = 'Design'
        design_cat.set_current_language('ar')
        design_cat.name = 'تصميم'
        design_cat.save()

        cloud_cat, _ = ServiceCategory.objects.get_or_create(slug='cloud')
        cloud_cat.set_current_language('en')
        cloud_cat.name = 'Cloud'
        cloud_cat.set_current_language('ar')
        cloud_cat.name = 'سحابة'
        cloud_cat.save()

        # 3. Services
        services_data = [
            {
                'slug': 'web-development',
                'category': web_cat,
                'short_description_en': 'High-performance web applications built with React and Django.',
                'short_description_ar': 'تطبيقات ويب عالية الأداء مبنية بـ React و Django.',
                'description_en': 'We build scalable, secure, and performant web applications using the latest technologies like React, Next.js, and Django. Our solutions are optimized for speed and user experience.',
                'description_ar': 'نبني تطبيقات ويب قابلة للتوسع وآمنة وعالية الأداء باستخدام أحدث التقنيات مثل React و Next.js و Django.',
                'icon': 'fa-code',
                'image': 'services/service-web.jpg',
                'is_featured': True,
                'name_en': 'Web Development',
                'name_ar': 'تطوير المواقع',
                'meta_title_en': 'Web Development Services',
                'meta_title_ar': 'خدمات تطوير المواقع',
                'meta_description_en': 'Professional web development services using React and Django.',
                'meta_description_ar': 'خدمات تطوير المواقع الاحترافية باستخدام React و Django.',
            },
            {
                'slug': 'mobile-app-development',
                'category': web_cat,
                'short_description_en': 'Native and cross-platform mobile experiences.',
                'short_description_ar': 'تجارب هاتف محمول أصلية وعبر المنصات.',
                'description_en': 'Exceptional mobile applications for iOS and Android using Flutter and React Native. We focus on smooth animations and intuitive user journeys.',
                'description_ar': 'تطبيقات هاتف استثنائية لـ iOS و Android باستخدام Flutter و React Native.',
                'icon': 'fa-mobile-alt',
                'image': 'services/service-mobile.jpg',
                'is_featured': True,
                'name_en': 'Mobile App Development',
                'name_ar': 'تطوير التطبيقات',
                'meta_title_en': 'Mobile App Development Services',
                'meta_title_ar': 'خدمات تطوير التطبيقات',
                'meta_description_en': 'Professional mobile app development for iOS and Android.',
                'meta_description_ar': 'تطوير تطبيقات محمولة احترافية لـ iOS و Android.',
            },
            {
                'slug': 'ui-ux-design',
                'category': design_cat,
                'short_description_en': 'User-centered design that converts.',
                'short_description_ar': 'تصميم مركز حول المستخدم يحول الزوار.',
                'description_en': 'Our design process starts with deep research to understand your users. We create beautiful, functional interfaces that drive engagement and growth.',
                'description_ar': 'عملية التصميم لدينا تبدأ ببحث عميق لفهم المستخدمين.',
                'icon': 'fa-paint-brush',
                'image': 'services/service-design.jpg',
                'is_featured': True,
                'name_en': 'UI/UX Design',
                'name_ar': 'تصميم UI/UX',
                'meta_title_en': 'UI/UX Design Services',
                'meta_title_ar': 'خدمات تصميم UI/UX',
                'meta_description_en': 'Professional UI/UX design services.',
                'meta_description_ar': 'خدمات تصميم UI/UX الاحترافية.',
            },
            {
                'slug': 'cloud-infrastructure',
                'category': cloud_cat,
                'short_description_en': 'Scalable AWS and Kubernetes solutions.',
                'short_description_ar': 'حلول قابلة للتوسع من AWS و Kubernetes.',
                'description_en': 'Modernize your infrastructure with our DevOps experts. We implement CI/CD pipelines and managed cloud services that scale with your business.',
                'description_ar': 'حدث البنية التحتية لديك مع خبراء DevOps لدينا.',
                'icon': 'fa-cloud',
                'image': 'services/service-cloud.jpg',
                'is_featured': True,
                'name_en': 'Cloud Infrastructure',
                'name_ar': 'البنية التحتية السحابية',
                'meta_title_en': 'Cloud Infrastructure Services',
                'meta_title_ar': 'خدمات البنية التحتية السحابية',
                'meta_description_en': 'Professional cloud infrastructure services using AWS and Kubernetes.',
                'meta_description_ar': 'خدمات البنية التحتية السحابية الاحترافية باستخدام AWS و Kubernetes.',
            }
        ]

        for s_data in services_data:
            # Extract translation fields
            name_en = s_data.pop('name_en')
            name_ar = s_data.pop('name_ar')
            short_description_en = s_data.pop('short_description_en')
            short_description_ar = s_data.pop('short_description_ar')
            description_en = s_data.pop('description_en')
            description_ar = s_data.pop('description_ar')
            meta_title_en = s_data.pop('meta_title_en')
            meta_title_ar = s_data.pop('meta_title_ar')
            meta_description_en = s_data.pop('meta_description_en')
            meta_description_ar = s_data.pop('meta_description_ar')
            
            service, created = Service.objects.get_or_create(
                slug=s_data['slug'],
                defaults=s_data
            )
            
            # Set translations
            service.set_current_language('en')
            service.name = name_en
            service.short_description = short_description_en
            service.description = description_en
            service.meta_title = meta_title_en
            service.meta_description = meta_description_en
            
            service.set_current_language('ar')
            service.name = name_ar
            service.short_description = short_description_ar
            service.description = description_ar
            service.meta_title = meta_title_ar
            service.meta_description = meta_description_ar
            
            service.save()
        
        self.stdout.write(self.style.SUCCESS('Services seeded.'))

        # 4. Project Categories
        fintech_cat, _ = ProjectCategory.objects.get_or_create(slug='fintech')
        fintech_cat.set_current_language('en')
        fintech_cat.name = 'Fintech'
        fintech_cat.set_current_language('ar')
        fintech_cat.name = 'تكنولوجيا مالية'
        fintech_cat.save()

        ecommerce_cat, _ = ProjectCategory.objects.get_or_create(slug='ecommerce')
        ecommerce_cat.set_current_language('en')
        ecommerce_cat.name = 'E-commerce'
        ecommerce_cat.set_current_language('ar')
        ecommerce_cat.name = 'تجارة إلكترونية'
        ecommerce_cat.save()

        health_cat, _ = ProjectCategory.objects.get_or_create(slug='healthcare')
        health_cat.set_current_language('en')
        health_cat.name = 'Healthcare'
        health_cat.set_current_language('ar')
        health_cat.name = 'رعاية صحية'
        health_cat.save()

        # 5. Projects
        projects_data = [
            {
                'slug': 'nova-banking-platform',
                'category': fintech_cat,
                'client_name_en': 'Nova Financial Group',
                'client_name_ar': 'مجموعة نوفا المالية',
                'short_description_en': 'A modern digital banking experience with real-time transactions.',
                'short_description_ar': 'تجربة مصرفية رقمية حديثة مع معاملات فورية.',
                'description_en': 'A comprehensive digital banking solution that revolutionizes how users manage their finances. Featuring AI-powered insights and instant transfers.',
                'description_ar': 'حل مصرفي شامل ي revolutionize طريقة إدارة المستخدمين لأموالهم.',
                'year': 2024,
                'is_featured': True,
                'website_url': 'https://example.com/nova',
                'title_en': 'Nova Banking Platform',
                'title_ar': 'منصة نوفا المصرفية',
                'meta_title_en': 'Nova Banking Platform - Fintech Solution',
                'meta_title_ar': 'منصة نوفا المصرفية - حل fintech',
                'meta_description_en': 'A modern digital banking experience.',
                'meta_description_ar': 'تجربة مصرفية رقمية حديثة.',
            },
            {
                'slug': 'luxe-marketplace',
                'category': ecommerce_cat,
                'client_name_en': 'Luxe Global',
                'client_name_ar': 'لوكس العالمية',
                'short_description_en': 'Premium e-commerce platform for high-end fashion.',
                'short_description_ar': 'منصة تجارة إلكترونية فاخرة للأزياء.',
                'description_en': 'A high-performance marketplace featuring headless architecture and seamless multi-currency support for a global audience.',
                'description_ar': 'سوق عالي الأداء مع架构 بدون رأس ودعم متعدد العملات.',
                'year': 2023,
                'is_featured': True,
                'website_url': 'https://example.com/luxe',
                'title_en': 'Luxe Marketplace',
                'title_ar': 'سوق لوكس',
                'meta_title_en': 'Luxe Marketplace - Premium E-commerce',
                'meta_title_ar': 'سوق لوكس - تجارة إلكترونية فاخرة',
                'meta_description_en': 'Premium e-commerce platform.',
                'meta_description_ar': 'منصة تجارة إلكترونية فاخرة.',
            },
            {
                'slug': 'medconnect-app',
                'category': health_cat,
                'client_name_en': 'City Health Hospital',
                'client_name_ar': 'مستشفى المدينة الصحي',
                'short_description_en': 'Telemedicine platform for secure consultations.',
                'short_description_ar': 'منصة telemedicine للتشاور الآمن.',
                'description_en': 'Connecting patients with specialists through encrypted video calls and integrated medical record management.',
                'description_ar': 'ربط المرضى بالأخصائيين عبر مكالمات فيديو مشفرة.',
                'year': 2024,
                'is_featured': True,
                'website_url': 'https://example.com/medconnect',
                'title_en': 'MedConnect App',
                'title_ar': 'تطبيق MedConnect',
                'meta_title_en': 'MedConnect - Telemedicine App',
                'meta_title_ar': 'MedConnect - تطبيق telemedicine',
                'meta_description_en': 'Telemedicine platform for secure consultations.',
                'meta_description_ar': 'منصة telemedicine للتشاور الآمن.',
            }
        ]

        for p_data in projects_data:
            # Extract translation fields
            title_en = p_data.pop('title_en')
            title_ar = p_data.pop('title_ar')
            client_name_en = p_data.pop('client_name_en')
            client_name_ar = p_data.pop('client_name_ar')
            short_description_en = p_data.pop('short_description_en')
            short_description_ar = p_data.pop('short_description_ar')
            description_en = p_data.pop('description_en')
            description_ar = p_data.pop('description_ar')
            meta_title_en = p_data.pop('meta_title_en')
            meta_title_ar = p_data.pop('meta_title_ar')
            meta_description_en = p_data.pop('meta_description_en')
            meta_description_ar = p_data.pop('meta_description_ar')
            
            project, created = Project.objects.get_or_create(
                slug=p_data['slug'],
                defaults=p_data
            )
            
            # Set translations
            project.set_current_language('en')
            project.title = title_en
            project.client_name = client_name_en
            project.short_description = short_description_en
            project.description = description_en
            project.meta_title = meta_title_en
            project.meta_description = meta_description_en
            
            project.set_current_language('ar')
            project.title = title_ar
            project.client_name = client_name_ar
            project.short_description = short_description_ar
            project.description = description_ar
            project.meta_title = meta_title_ar
            project.meta_description = meta_description_ar
            
            project.save()

        self.stdout.write(self.style.SUCCESS('Projects seeded.'))

        # 6. Testimonials
        testimonials_data = [
            {
                'client_name_en': 'Sarah Johnson',
                'client_name_ar': 'سارة جونسون',
                'company_en': 'Nova Financial',
                'company_ar': 'نوفا المالية',
                'position_en': 'CTO',
                'position_ar': 'الirector التقني',
                'quote_en': 'Bloom Digital transformed our legacy systems into a modern, scalable platform. Their expertise in microservices is unmatched.',
                'quote_ar': 'حول بلوم ديجيتال أنظمة لدينا القديمة إلى منصة حديثة وقابلة للتوسع.',
                'rating': 5
            },
            {
                'client_name_en': 'Ahmed Mansour',
                'client_name_ar': 'أحمد منصور',
                'company_en': 'Luxe Global',
                'company_ar': 'لوكس العالمية',
                'position_en': 'Founder',
                'position_ar': 'المؤسس',
                'quote_en': 'The attention to detail in the UI/UX design and the speed of the final product exceeded our expectations.',
                'quote_ar': 'الاهتمام بالتفاصيل في تصميم UI/UX وسرعة المنتج النهائي تجاوز توقعاتنا.',
                'rating': 5
            }
        ]

        for i, t_data in enumerate(testimonials_data):
            client_name_en = t_data.pop('client_name_en')
            client_name_ar = t_data.pop('client_name_ar')
            company_en = t_data.pop('company_en')
            company_ar = t_data.pop('company_ar')
            position_en = t_data.pop('position_en')
            position_ar = t_data.pop('position_ar')
            quote_en = t_data.pop('quote_en')
            quote_ar = t_data.pop('quote_ar')
            
            # Use a simple approach - get or create by rating (since we don't have unique translated fields)
            testimonial, created = Testimonial.objects.get_or_create(
                rating=t_data['rating'],
                defaults=t_data
            )
            
            # Set translations
            testimonial.set_current_language('en')
            testimonial.client_name = client_name_en
            testimonial.company = company_en
            testimonial.position = position_en
            testimonial.quote = quote_en
            
            testimonial.set_current_language('ar')
            testimonial.client_name = client_name_ar
            testimonial.company = company_ar
            testimonial.position = position_ar
            testimonial.quote = quote_ar
            
            testimonial.save()

        self.stdout.write(self.style.SUCCESS('Testimonials seeded.'))

        # 7. Job Postings
        jobs_data = [
            {
                'slug': 'senior-python-developer',
                'job_type': 'full_time',
                'is_featured': True,
                'is_active': True,
                'salary_range': '$80,000 - $120,000',
                'title_en': 'Senior Python Developer',
                'title_ar': 'مطور بايثون senior',
                'department_en': 'Engineering',
                'department_ar': 'الهندسة',
                'location_en': 'Remote',
                'location_ar': 'عن بُعد',
                'description_en': 'We are looking for an experienced Python developer to join our team.',
                'description_ar': 'نحن نبحث عن مطور بايثون خبير للانضمام إلى فريقنا.',
                'requirements_en': '5+ years experience with Python, Django, PostgreSQL',
                'requirements_ar': 'خبرة 5+ سنوات مع Python و Django و PostgreSQL',
                'responsibilities_en': 'Develop scalable web applications, mentor junior developers',
                'responsibilities_ar': 'تطوير تطبيقات ويب قابلة للتطوير، إرشاد المطورين المبتدئين',
            },
            {
                'slug': 'frontend-react-developer',
                'job_type': 'full_time',
                'is_featured': True,
                'is_active': True,
                'salary_range': '$60,000 - $90,000',
                'title_en': 'Frontend React Developer',
                'title_ar': 'مطور React للواجهة الأمامية',
                'department_en': 'Engineering',
                'department_ar': 'الهندسة',
                'location_en': 'Remote',
                'location_ar': 'عن بُعد',
                'description_en': 'Join our team to build beautiful React applications.',
                'description_ar': 'انضم إلى فريقنا لبناء تطبيقات React جميلة.',
                'requirements_en': '3+ years experience with React, TypeScript, Next.js',
                'requirements_ar': 'خبرة 3+ سنوات مع React و TypeScript و Next.js',
                'responsibilities_en': 'Build responsive UI components, collaborate with designers',
                'responsibilities_ar': 'بناء مكونات UI متجاوبة، التعاون مع المصممين',
            },
            {
                'slug': 'devops-engineer',
                'job_type': 'full_time',
                'is_featured': False,
                'is_active': True,
                'salary_range': '$90,000 - $130,000',
                'title_en': 'DevOps Engineer',
                'title_ar': 'مهندس DevOps',
                'department_en': 'Operations',
                'department_ar': 'العمليات',
                'location_en': 'Remote',
                'location_ar': 'عن بُعد',
                'description_en': 'We need a DevOps engineer to manage our cloud infrastructure.',
                'description_ar': 'نحتاج مهندس DevOps لإدارة البنية التحتية السحابية.',
                'requirements_en': 'Experience with AWS, Kubernetes, Docker, CI/CD',
                'requirements_ar': 'خبرة مع AWS و Kubernetes و Docker و CI/CD',
                'responsibilities_en': 'Manage cloud infrastructure, implement automation',
                'responsibilities_ar': 'إدارة البنية التحتية السحابية، تنفيذ الأتمتة',
            },
        ]

        for j_data in jobs_data:
            title_en = j_data.pop('title_en')
            title_ar = j_data.pop('title_ar')
            department_en = j_data.pop('department_en')
            department_ar = j_data.pop('department_ar')
            location_en = j_data.pop('location_en')
            location_ar = j_data.pop('location_ar')
            description_en = j_data.pop('description_en')
            description_ar = j_data.pop('description_ar')
            requirements_en = j_data.pop('requirements_en')
            requirements_ar = j_data.pop('requirements_ar')
            responsibilities_en = j_data.pop('responsibilities_en')
            responsibilities_ar = j_data.pop('responsibilities_ar')
            
            job, created = JobPosting.objects.get_or_create(
                slug=j_data['slug'],
                defaults=j_data
            )
            
            job.set_current_language('en')
            job.title = title_en
            job.department = department_en
            job.location = location_en
            job.description = description_en
            job.requirements = requirements_en
            job.responsibilities = responsibilities_en
            
            job.set_current_language('ar')
            job.title = title_ar
            job.department = department_ar
            job.location = location_ar
            job.description = description_ar
            job.requirements = requirements_ar
            job.responsibilities = responsibilities_ar
            
            job.save()

        self.stdout.write(self.style.SUCCESS('Jobs seeded.'))
        self.stdout.write(self.style.SUCCESS('Database seeding completed successfully!'))