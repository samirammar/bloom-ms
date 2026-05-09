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
                'content_en': '<h2>What Are Microservices?</h2>\n<p><strong>Microservices architecture</strong> has become the backbone of modern software development. By breaking down monolithic applications into smaller, independent services, organizations can achieve unprecedented levels of scalability and maintainability.</p>\n<p>Each service in a microservices architecture is independently deployable, allowing teams to work on different services simultaneously without interfering with each other. This leads to faster development cycles and more frequent deployments.</p>\n<h2>Key Benefits</h2>\n<p>Here are the main advantages of adopting a microservices architecture:</p>\n<ul>\n<li><strong>Independent scaling</strong> — Scale services based on demand</li>\n<li><strong>Technology diversity</strong> — Each service can use the best tech stack for its purpose</li>\n<li><strong>Fault isolation</strong> — A failure in one service doesn\'t bring down the entire system</li>\n<li><strong>Easier onboarding</strong> — New developers can work on smaller, focused codebases</li>\n</ul>\n<h2>Why Choose Bloom?</h2>\n<p>At <strong>Bloom</strong>, we have extensive experience designing and implementing microservices architectures for enterprises of all sizes. Our team follows industry best practices to ensure your microservices are secure, observable, and cost-effective.</p>\n<pre><code># Example: Flask-based microservice\nfrom flask import Flask\napp = Flask(__name__)\n\n@app.route(\'/api/health\')\ndef health_check():\n    return {&quot;status&quot;: &quot;healthy&quot;}\n</code></pre>\n',
                'content_ar': '<h2>ما هي الخدمات المصغرة؟</h2>\n<p><strong>هندسة الخدمات المصغرة</strong> أصبحت العمود الفقري لتطوير البرمجيات الحديثة. من خلال تقسيم التطبيقات المتجانسة إلى خدمات أصغر ومستقلة، يمكن للمؤسسات تحقيق مستويات غير مسبوقة من قابلية التوسع والصيانة.</p>\n<p>كل خدمة في هندسة الخدمات المصغرة قابلة للنشر بشكل مستقل، مما يسمح للفرق بالعمل على خدمات مختلفة في وقت واحد دون التدخل في عمل بعضهم البعض.</p>\n<h2>الفوائد الرئيسية</h2>\n<p>إليك المزايا الرئيسية لاعتماد بنية الخدمات المصغرة:</p>\n<ul>\n<li><strong>توسيع مستقل</strong> — ضبط موارد الخدمات حسب الطلب</li>\n<li><strong>تنوع التكنولوجيا</strong> — لكل خدمة أفضل أدواتها</li>\n<li><strong>عزل الأعطال</strong> — تعطل خدمة لا يعني تعطل الكل</li>\n<li><strong>سهولة الانضمام</strong> — مطورون جدد يعملون على قواعد بيانات أصغر</li>\n</ul>\n<h2>لماذا بلوم؟</h2>\n<p>في <strong>بلوم</strong>، لدينا خبرة واسعة في تصميم وتنفيذ بنى الخدمات المصغرة للمؤسسات من جميع الأحجام. يتبع فريقنا أفضل ممارسات الصناعة لضمان أن خدماتك المصغرة آمنة وقابلة للمراقبة وفعالة من حيث التكلفة.</p>\n',
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
                'content_en': '<h2>Why Django?</h2>\n<p><strong>Django</strong> continues to be one of the most popular web frameworks for building robust applications. Here are our top best practices for Django development in 2024.</p>\n<h2>1. Environment Variables</h2>\n<p>Never hardcode sensitive data like API keys or database credentials. Use <code>django-environ</code> or <code>python-decouple</code>:</p>\n<pre><code class="language-python"># settings.py\nimport environ\nenv = environ.Env()\nSECRET_KEY = env(\'DJANGO_SECRET_KEY\')\n</code></pre>\n<h2>2. Optimize Database Queries</h2>\n<p>Use <code>select_related()</code> and <code>prefetch_related()</code> to reduce database queries. Always profile with <strong>Django Debug Toolbar</strong>.</p>\n<h2>3. Implement Caching</h2>\n<p>Use Django\'s cache framework with <strong>Redis</strong> or <strong>Memcached</strong> to improve response times.</p>\n<h2>4. Write Tests!</h2>\n<p>Write unit tests, integration tests, and end-to-end tests. Aim for at least <strong>80% code coverage</strong>.</p>\n<pre><code class="language-python">def test_home_page():\n    response = client.get(\'/\')\n    assert response.status_code == 200\n</code></pre>\n<h2>5. Keep Apps Focused</h2>\n<p>Each Django app should have a <strong>single responsibility</strong>. Follow the Unix philosophy: do one thing well.</p>\n',
                'content_ar': '<h2>لماذا Django؟</h2>\n<p><strong>Django</strong> يستمر في كونه أحد أكثر أطر العمل شيوعاً لبناء تطبيقات الويب القوية. إليك أفضل ممارساتنا لتطوير Django في 2024.</p>\n<h2>1. متغيرات البيئة</h2>\n<p>لا تقم أبداً بتضمين البيانات الحساسة مثل مفاتيح API أو بيانات اعتماد قاعدة البيانات في الكود. استخدم <code>django-environ</code> أو <code>python-decouple</code>:</p>\n<pre><code class="language-python"># settings.py\nimport environ\nenv = environ.Env()\nSECRET_KEY = env(\'DJANGO_SECRET_KEY\')\n</code></pre>\n<h2>2. تحسين الاستعلامات</h2>\n<p>استخدم <code>select_related()</code> و <code>prefetch_related()</code> لتقليل عدد الاستعلامات. حلل الأداء باستخدام <strong>Django Debug Toolbar</strong>.</p>\n<h2>3. التخزين المؤقت</h2>\n<p>استخدم إطار التخزين المؤقت في Django مع <strong>Redis</strong> أو <strong>Memcached</strong> لتحسين أوقات الاستجابة.</p>\n<h2>4. اكتب الاختبارات!</h2>\n<p>اكتب اختبارات الوحدة واختبارات التكامل. استهدف <strong>تغطية 80%</strong> من الكود.</p>\n<h2>5. تطبيقات مركزة</h2>\n<p>لكل تطبيق Django <strong>مسؤولية واحدة</strong>. اتبع فلسفة Unix: أتقن شيئاً واحداً.</p>\n',
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
                'content_en': '<h2>What is CI/CD?</h2>\n<p><strong>Continuous Integration and Continuous Deployment (CI/CD)</strong> is essential for modern software development teams. <strong>GitHub Actions</strong> provides a powerful platform for automating your entire deployment workflow.</p>\n<h2>Step 1: Define Your Workflow</h2>\n<p>Create a <code>.github/workflows</code> directory in your repository and add a YAML file:</p>\n<pre><code class="language-yaml">name: CI/CD Pipeline\non: [push]\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - run: pip install -r requirements.txt\n      - run: pytest\n</code></pre>\n<h2>Step 2: Set Up Testing</h2>\n<p>Configure your workflow to run tests automatically on every push. This ensures code changes don\'t break existing functionality.</p>\n<h2>Step 3: Build &amp; Package</h2>\n<p>Set up build steps to compile your application and create deployable artifacts. Use <strong>caching</strong> to speed up builds.</p>\n<h2>Step 4: Deploy</h2>\n<p>Deploy to your target environment after successful tests. Use <strong>GitHub Secrets</strong> for sensitive data.</p>\n<p>At <strong>Bloom</strong>, we use GitHub Actions extensively across all projects, resulting in shorter release cycles and higher code quality.</p>\n',
                'content_ar': '<h2>ما هو CI/CD؟</h2>\n<p><strong>التكامل المستمر والنشر المستمر (CI/CD)</strong> أساسيان لفرق تطوير البرمجيات الحديثة. <strong>GitHub Actions</strong> يوفر منصة قوية لأتمتة سير عمل النشر.</p>\n<h2>الخطوة 1: تحديد سير العمل</h2>\n<p>أنشئ مجلد <code>.github/workflows</code> وأضف ملف YAML:</p>\n<pre><code class="language-yaml">name: CI/CD Pipeline\non: [push]\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - run: pytest\n</code></pre>\n<h2>الخطوة 2: إعداد الاختبارات</h2>\n<p>شغّل الاختبارات تلقائياً مع كل push لضمان عدم كسر التغييرات للوظائف الحالية.</p>\n<h2>الخطوة 3: البناء والنشر</h2>\n<p>قم بإعداد خطوات البناء وإنشاء القطع القابلة للنشر. استخدم <strong>التخزين المؤقت</strong> لتسريع البناء.</p>\n<h2>الخطوة 4: النشر</h2>\n<p>انشر إلى بيئتك المستهدفة بعد نجاح الاختبارات. استخدم <strong>أسرار GitHub</strong> للبيانات الحساسة.</p>\n<p>في <strong>بلوم</strong>، نستخدم GitHub Actions في جميع مشاريعنا.</p>\n',
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
                'content_en': '<h2>The Evolution of Design</h2>\n<p>User experience continues to evolve rapidly. Here are the <strong>top UI/UX design trends</strong> defining 2024.</p>\n<h2>1. AI-Powered Personalization</h2>\n<p>Interfaces that adapt to user behavior in <strong>real-time</strong>, offering personalized content and recommendations using machine learning.</p>\n<h2>2. Micro-interactions</h2>\n<p>Subtle animations and feedback mechanisms make interfaces feel <strong>alive and responsive</strong>. Every click, hover, and swipe should feel intentional.</p>\n<h2>3. Dark Mode 2.0</h2>\n<p>More sophisticated dark themes with <strong>better contrast</strong>, custom color schemes, and smooth transitions between modes.</p>\n<h2>4. 3D Elements</h2>\n<p>Subtle 3D elements, depth effects, and parallax scrolling that create <strong>immersive experiences</strong> without overwhelming the user.</p>\n<blockquote>\n<p>&quot;Good design is as little design as possible.&quot; — Dieter Rams</p>\n</blockquote>\n<h2>5. Voice Interfaces</h2>\n<p>Voice commands and conversational interfaces are becoming mainstream, especially in mobile and IoT applications.</p>\n<h2>6. Glassmorphism</h2>\n<p>The glass effect continues to evolve with better accessibility and more refined implementations.</p>\n<p>At <strong>Bloom</strong>, we stay at the forefront of design trends to deliver interfaces that are beautiful, functional, and accessible.</p>\n',
                'content_ar': '<h2>تطور التصميم</h2>\n<p>تستمر تجربة المستخدم في التطور بسرعة. إليك <strong>أهم اتجاهات تصميم UI/UX</strong> التي تحدد عام 2024.</p>\n<h2>1. التخصيص بالذكاء الاصطناعي</h2>\n<p>واجهات تتكيف مع سلوك المستخدم في <strong>الوقت الفعلي</strong>، وتقدم محتوى وتوصيات مخصصة باستخدام التعلم الآلي.</p>\n<h2>2. التفاعلات الدقيقة</h2>\n<p>رسوم متحركة دقيقة وآليات ردود فعل تجعل الواجهات <strong>حية ومستجيبة</strong>. كل نقرة وتحويم وتمرير يجب أن يكون مقصوداً.</p>\n<h2>3. الوضع الداكن 2.0</h2>\n<p>سمات داكنة أكثر تطوراً مع <strong>تباين أفضل</strong> وأنظمة ألوان مخصصة وانتقالات سلسة.</p>\n<h2>4. العناصر ثلاثية الأبعاد</h2>\n<p>عناصر ثلاثية الأبعاد دقيقة وتأثيرات عمق تخلق <strong>تجارب غامرة</strong> دون إرباك المستخدم.</p>\n<h2>5. الواجهات الصوتية</h2>\n<p>الأوامر الصوتية والواجهات التحادثية أصبحت سائدة في تطبيقات الهاتف وإنترنت الأشياء.</p>\n<h2>6. الزجاجية</h2>\n<p>تأثير الزجاج يتطور مع إمكانية وصول أفضل وتنفيذات أكثر دقة.</p>\n<p>في <strong>بلوم</strong>، نبقى في طليعة اتجاهات التصميم لنقدم واجهات جميلة ووظيفية.</p>\n',
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