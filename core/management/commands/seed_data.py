from django.core.management.base import BaseCommand
from core.models import SiteSettings
from projects.models import Project, ProjectCategory, Testimonial
from services.models import Service, ServiceCategory
from jobs.models import JobPosting
from blog.models import BlogCategory, BlogPost
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

        # 8. Blog Categories
        tech_cat, _ = BlogCategory.objects.get_or_create(slug='technology')
        tech_cat.set_current_language('en')
        tech_cat.name = 'Technology'
        tech_cat.set_current_language('ar')
        tech_cat.name = 'تكنولوجيا'
        tech_cat.save()

        arch_cat, _ = BlogCategory.objects.get_or_create(slug='architecture')
        arch_cat.set_current_language('en')
        arch_cat.name = 'Architecture'
        arch_cat.set_current_language('ar')
        arch_cat.name = 'هندسة برمجيات'
        arch_cat.save()

        devops_cat, _ = BlogCategory.objects.get_or_create(slug='devops')
        devops_cat.set_current_language('en')
        devops_cat.name = 'DevOps'
        devops_cat.set_current_language('ar')
        devops_cat.name = 'ديف أوبس'
        devops_cat.save()

        self.stdout.write(self.style.SUCCESS('Blog Categories seeded.'))

        # 9. Blog Posts
        blog_posts_data = [
            {
                'slug': 'why-microservices-matter',
                'category': arch_cat,
                'is_featured': True,
                'is_published': True,
                'title_en': 'Why Microservices Architecture Matters in 2024',
                'title_ar': 'لماذا تهم هندسة الخدمات المصغرة في 2024',
                'short_description_en': 'Discover how microservices can transform your business with scalability, resilience, and faster time-to-market.',
                'short_description_ar': 'اكتشف كيف يمكن للخدمات المصغرة تحويل عملك من خلال قابلية التوسع والمرونة والوصول الأسرع إلى السوق.',
                'content_en': 'Microservices architecture has become the backbone of modern software development. By breaking down monolithic applications into smaller, independent services, organizations can achieve unprecedented levels of scalability and maintainability.\n\nEach service in a microservices architecture is independently deployable, allowing teams to work on different services simultaneously without interfering with each other. This leads to faster development cycles and more frequent deployments.\n\nKey benefits include:\n- Independent scaling of services based on demand\n- Technology diversity - each service can use the best tech stack for its purpose\n- Improved fault isolation - a failure in one service doesn\'t bring down the entire system\n- Easier onboarding for new developers due to smaller codebases\n\nAt Bloom, we have extensive experience designing and implementing microservices architectures for enterprises of all sizes. Our team follows industry best practices to ensure your microservices are secure, observable, and cost-effective.',
                'content_ar': 'أصبحت هندسة الخدمات المصغرة العمود الفقري لتطوير البرمجيات الحديثة. من خلال تقسيم التطبيقات المتجانسة إلى خدمات أصغر ومستقلة، يمكن للمؤسسات تحقيق مستويات غير مسبوقة من قابلية التوسع والصيانة.\n\nكل خدمة في هندسة الخدمات المصغرة قابلة للنشر بشكل مستقل، مما يسمح للفرق بالعمل على خدمات مختلفة في وقت واحد دون التدخل في عمل بعضهم البعض. يؤدي هذا إلى دورات تطوير أسرع ونشر أكثر تواتراً.\n\nتشمل الفوائد الرئيسية:\n- توسيع نطاق الخدمات بشكل مستقل حسب الطلب\n- تنوع التكنولوجيا - يمكن لكل خدمة استخدام أفضل مجموعة تقنية لغرضها\n- تحسين عزل الأعطال - فشل خدمة واحدة لا يعطل النظام بأكمله\n- سهولة انضمام المطورين الجدد بسبب قواعد البيانات الأصغر\n\nفي بلوم، لدينا خبرة واسعة في تصميم وتنفيذ بنى الخدمات المصغرة للمؤسسات من جميع الأحجام. يتبع فريقنا أفضل ممارسات الصناعة لضمان أن خدماتك المصغرة آمنة وقابلة للمراقبة وفعالة من حيث التكلفة.',
                'tags_en': 'microservices,architecture,scalability',
                'tags_ar': 'خدمات مصغرة,هندسة برمجيات,قابلية التوسع',
                'meta_title_en': 'Why Microservices Architecture Matters | Bloom Digital Studio',
                'meta_title_ar': 'لماذا تهم الخدمات المصغرة | بلوم ديجيتال',
                'meta_description_en': 'Learn why microservices architecture is essential for modern software development.',
                'meta_description_ar': 'تعرف على أهمية هندسة الخدمات المصغرة في تطوير البرمجيات الحديثة.',
            },
            {
                'slug': 'django-best-practices',
                'category': tech_cat,
                'is_featured': True,
                'is_published': True,
                'title_en': 'Django Best Practices for 2024',
                'title_ar': 'أفضل ممارسات Django لعام 2024',
                'short_description_en': 'A comprehensive guide to building secure, scalable, and maintainable Django applications.',
                'short_description_ar': 'دليل شامل لبناء تطبيقات Django آمنة وقابلة للتوسع وسهلة الصيانة.',
                'content_en': 'Django continues to be one of the most popular web frameworks for building robust web applications. Here are our top best practices for Django development in 2024.\n\n1. Use Environment Variables: Never hardcode sensitive data like API keys, database credentials, or secret keys. Use environment variables with django-environ or python-decouple.\n\n2. Optimize Database Queries: Use select_related() and prefetch_related() to reduce the number of database queries. Always profile your queries using Django Debug Toolbar.\n\n3. Implement Proper Caching: Use Django\'s cache framework with Redis or Memcached to significantly improve response times for frequently accessed data.\n\n4. Write Comprehensive Tests: Use Django\'s test framework to write unit tests, integration tests, and end-to-end tests. Aim for at least 80% code coverage.\n\n5. Follow the App Pattern: Keep your code organized by following Django\'s app structure. Each app should have a single responsibility.',
                'content_ar': 'يستمر Django في كونه أحد أكثر أطر العمل شيوعاً لبناء تطبيقات الويب القوية. إليك أفضل ممارساتنا لتطوير Django في 2024.\n\n1. استخدام متغيرات البيئة: لا تقم أبداً بتضمين البيانات الحساسة مثل مفاتيح API أو بيانات اعتماد قاعدة البيانات أو المفاتيح السرية في الكود. استخدم متغيرات البيئة مع django-environ أو python-decouple.\n\n2. تحسين استعلامات قاعدة البيانات: استخدم select_related() و prefetch_related() لتقليل عدد استعلامات قاعدة البيانات. قم دائماً بتحليل استعلاماتك باستخدام Django Debug Toolbar.\n\n3. تطبيق التخزين المؤقت المناسب: استخدم إطار التخزين المؤقت في Django مع Redis أو Memcached لتحسين أوقات الاستجابة بشكل كبير للبيانات التي يتم الوصول إليها بشكل متكرر.\n\n4. كتابة اختبارات شاملة: استخدم إطار الاختبار في Django لكتابة اختبارات الوحدة واختبارات التكامل واختبارات النهاية إلى النهاية. استهدف تغطية كود بنسبة 80٪ على الأقل.\n\n5. اتباع نمط التطبيقات: حافظ على تنظيم كودك باتباع هيكل تطبيقات Django. يجب أن يكون لكل تطبيق مسؤولية واحدة.',
                'tags_en': 'django,python,web-development,best-practices',
                'tags_ar': 'django,بايثون,تطوير الويب,أفضل الممارسات',
                'meta_title_en': 'Django Best Practices 2024 | Bloom Digital Studio',
                'meta_title_ar': 'أفضل ممارسات Django 2024 | بلوم ديجيتال',
                'meta_description_en': 'Comprehensive Django best practices guide for building modern web applications.',
                'meta_description_ar': 'دليل شامل لأفضل ممارسات Django لبناء تطبيقات ويب حديثة.',
            },
            {
                'slug': 'ci-cd-pipeline-setup',
                'category': devops_cat,
                'is_featured': False,
                'is_published': True,
                'title_en': 'Setting Up a CI/CD Pipeline with GitHub Actions',
                'title_ar': 'إعداد خط أنابيب CI/CD مع GitHub Actions',
                'short_description_en': 'Learn how to automate your deployment pipeline using GitHub Actions for faster and more reliable releases.',
                'short_description_ar': 'تعلم كيفية أتمتة خط أنابيب النشر باستخدام GitHub Actions لإصدارات أسرع وأكثر موثوقية.',
                'content_en': 'Continuous Integration and Continuous Deployment (CI/CD) is essential for modern software development teams. GitHub Actions provides a powerful platform for automating your entire deployment workflow.\n\nStep 1: Define Your Workflow\nCreate a .github/workflows directory in your repository and add a YAML file defining your workflow. Specify the trigger events (push, pull request, etc.) and the jobs to run.\n\nStep 2: Set Up Testing\nConfigure your workflow to run tests automatically on every push. This ensures that code changes don\'t break existing functionality.\n\nStep 3: Build and Package\nSet up build steps to compile your application and create deployable artifacts. Use caching to speed up subsequent builds.\n\nStep 4: Deploy\nConfigure deployment to your target environment (staging, production) after successful tests and builds. Use environment secrets for sensitive data.\n\nAt Bloom, we use GitHub Actions extensively across all our projects, resulting in shorter release cycles and higher code quality.',
                'content_ar': 'التكامل المستمر والنشر المستمر (CI/CD) أساسيان لفرق تطوير البرمجيات الحديثة. يوفر GitHub Actions منصة قوية لأتمتة سير عمل النشر بالكامل.\n\nالخطوة 1: تحديد سير العمل\nقم بإنشاء دليل .github/workflows في مستودعك وأضف ملف YAML يحدد سير عملك. حدد أحداث التشغيل (push، طلب سحب، إلخ) والمهام التي سيتم تشغيلها.\n\nالخطوة 2: إعداد الاختبارات\nقم بتكوين سير العمل لتشغيل الاختبارات تلقائياً مع كل push. يضمن هذا عدم كسر تغييرات الكود للوظائف الحالية.\n\nالخطوة 3: البناء والتعبئة\nقم بإعداد خطوات البناء لترجمة تطبيقك وإنشاء القطع القابلة للنشر. استخدم التخزين المؤقت لتسريع عمليات البناء اللاحقة.\n\nالخطوة 4: النشر\nقم بتكوين النشر إلى بيئتك المستهدفة (التجريبية، الإنتاجية) بعد نجاح الاختبارات والبناء. استخدم أسرار البيئة للبيانات الحساسة.\n\nفي بلوم، نستخدم GitHub Actions على نطاق واسع في جميع مشاريعنا، مما يؤدي إلى دورات إصدار أقصر وجودة كود أعلى.',
                'tags_en': 'devops,ci-cd,github-actions,automation',
                'tags_ar': 'ديف أوبس,CI/CD,github-actions,أتمتة',
                'meta_title_en': 'CI/CD Pipeline with GitHub Actions | Bloom Digital Studio',
                'meta_title_ar': 'خط أنابيب CI/CD مع GitHub Actions | بلوم ديجيتال',
                'meta_description_en': 'Step-by-step guide to setting up CI/CD pipeline with GitHub Actions.',
                'meta_description_ar': 'دليل خطوة بخطوة لإعداد خط أنابيب CI/CD مع GitHub Actions.',
            },
            {
                'slug': 'ui-ux-trends-2024',
                'category': tech_cat,
                'is_featured': False,
                'is_published': True,
                'title_en': 'Top UI/UX Design Trends to Watch in 2024',
                'title_ar': 'أهم اتجاهات تصميم UI/UX في 2024',
                'short_description_en': 'Explore the latest design trends that are shaping user experiences across digital products.',
                'short_description_ar': 'استكشف أحدث اتجاهات التصميم التي تشكل تجارب المستخدم عبر المنتجات الرقمية.',
                'content_en': 'User experience continues to evolve rapidly. Here are the top UI/UX design trends that are defining 2024.\n\n1. AI-Powered Personalization: Interfaces that adapt to user behavior in real-time, offering personalized content and recommendations.\n\n2. Micro-interactions: Subtle animations and feedback mechanisms that make interfaces feel alive and responsive.\n\n3. Dark Mode 2.0: More sophisticated dark themes with better contrast, custom color schemes, and smooth transitions between modes.\n\n4. 3D Elements and Depth: Subtle 3D elements, depth effects, and parallax scrolling that create immersive experiences.\n\n5. Voice User Interfaces: Voice commands and conversational interfaces are becoming mainstream, especially in mobile and IoT applications.\n\n6. Glassmorphism: The glass effect continues to evolve with better accessibility and more refined implementations.\n\nAt Bloom, we stay at the forefront of design trends to deliver interfaces that are not only beautiful but also highly functional and accessible.',
                'content_ar': 'تستمر تجربة المستخدم في التطور بسرعة. إليك أهم اتجاهات تصميم UI/UX التي تحدد عام 2024.\n\n1. التخصيص بالذكاء الاصطناعي: واجهات تتكيف مع سلوك المستخدم في الوقت الفعلي، وتقدم محتوى وتوصيات مخصصة.\n\n2. التفاعلات الدقيقة: رسوم متحركة دقيقة وآليات ردود فعل تجعل الواجهات تبدو حية ومستجيبة.\n\n3. الوضع الداكن 2.0: سمات داكنة أكثر تطوراً مع تباين أفضل وأنظمة ألوان مخصصة وانتقالات سلسة بين الأوضاع.\n\n4. عناصر ثلاثية الأبعاد والعمق: عناصر ثلاثية الأبعاد دقيقة وتأثيرات عمق وتمرير parallax تخلق تجارب غامرة.\n\n5. واجهات المستخدم الصوتية: الأوامر الصوتية والواجهات التحادثية أصبحت سائدة، خاصة في تطبيقات الهاتف وإنترنت الأشياء.\n\n6. الزجاجية: تأثير الزجاج يستمر في التطور مع إمكانية وصول أفضل وتنفيذات أكثر دقة.\n\nفي بلوم، نبقى في طليعة اتجاهات التصميم لنقدم واجهات ليست جميلة فحسب بل أيضاً عالية الوظائف وسهلة الوصول.',
                'tags_en': 'ui-ux,design,trends,user-experience',
                'tags_ar': 'UI-UX,تصميم,اتجاهات,تجربة المستخدم',
                'meta_title_en': 'UI/UX Design Trends 2024 | Bloom Digital Studio',
                'meta_title_ar': 'اتجاهات تصميم UI/UX 2024 | بلوم ديجيتال',
                'meta_description_en': 'Discover the top UI/UX design trends shaping digital products in 2024.',
                'meta_description_ar': 'اكتشف أهم اتجاهات تصميم UI/UX التي تشكل المنتجات الرقمية في 2024.',
            },
        ]

        for bp_data in blog_posts_data:
            title_en = bp_data.pop('title_en')
            title_ar = bp_data.pop('title_ar')
            short_description_en = bp_data.pop('short_description_en')
            short_description_ar = bp_data.pop('short_description_ar')
            content_en = bp_data.pop('content_en')
            content_ar = bp_data.pop('content_ar')
            tags_en = bp_data.pop('tags_en')
            tags_ar = bp_data.pop('tags_ar')
            meta_title_en = bp_data.pop('meta_title_en')
            meta_title_ar = bp_data.pop('meta_title_ar')
            meta_description_en = bp_data.pop('meta_description_en')
            meta_description_ar = bp_data.pop('meta_description_ar')

            post, created = BlogPost.objects.get_or_create(
                slug=bp_data['slug'],
                defaults=bp_data,
            )

            post.set_current_language('en')
            post.title = title_en
            post.short_description = short_description_en
            post.content = content_en
            post.tags = tags_en
            post.meta_title = meta_title_en
            post.meta_description = meta_description_en

            post.set_current_language('ar')
            post.title = title_ar
            post.short_description = short_description_ar
            post.content = content_ar
            post.tags = tags_ar
            post.meta_title = meta_title_ar
            post.meta_description = meta_description_ar

            post.save()

        self.stdout.write(self.style.SUCCESS('Blog Posts seeded.'))
        self.stdout.write(self.style.SUCCESS('Database seeding completed successfully!'))