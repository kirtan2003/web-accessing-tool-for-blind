import pandas as pd
import numpy as np

# Lists of various categories for generating queries
queries = [
    'What is the capital of {}?',
    'How does {} work?',
    'What is the stock price of {}?',
    'How to learn {} programming?',
    'What is {} in data science?',
    'Explain the history of {}.',
    'What are the health benefits of {}?',
    'How to invest in {}?',
    'What are the latest trends in {}?',
    'How is {} affecting the global economy?',
    'What are the rules of {}?',
    'Who won the last {} championship?',
    'What are the techniques used in {}?',
    'How to train for {}?',
    'What are the health benefits of practicing {}?',
    'Who are the top athletes in {}?',
    'What are the strategies for winning in {}?',
    'What are the most popular {} events?',
    'How is technology changing {}?',
    'What are the equipment needed for {}?',
]

countries = ['India', 'USA', 'France', 'Germany', 'Brazil', 'Japan', 'China', 'Russia', 'Canada', 'Australia', 'Italy', 'Spain', 'Mexico', 'South Korea', 'South Africa']
technologies = ['photosynthesis', 'quantum computing', 'blockchain', 'machine learning', 'neural networks', 'artificial intelligence', 'robotics', 'biotechnology', 'nanotechnology', 'renewable energy', '3D printing', 'Internet of Things', 'augmented reality', 'virtual reality', 'cybersecurity']
companies = ['Apple', 'Google', 'Amazon', 'Tesla', 'Facebook', 'Microsoft', 'IBM', 'Intel', 'NVIDIA', 'Samsung', 'Sony', 'Oracle', 'SAP', 'Uber', 'Airbnb']
programming_languages = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'Swift', 'Go', 'R', 'PHP', 'TypeScript', 'Kotlin', 'Scala', 'Perl', 'Lua', 'Elixir']
data_science_terms = ['regression', 'classification', 'clustering', 'deep learning', 'neural networks', 'big data', 'data visualization', 'predictive analytics', 'machine learning', 'statistics', 'natural language processing', 'computer vision', 'reinforcement learning', 'bioinformatics', 'quantum computing']
histories = ['Rome', 'Egypt', 'Greece', 'China', 'India', 'USA', 'France', 'Germany', 'Russia', 'Japan', 'Persia', 'Mongolia', 'Vikings', 'Mayans', 'Aztecs']
health_topics = ['yoga', 'meditation', 'running', 'swimming', 'cycling', 'weight lifting', 'paleo diet', 'veganism', 'ketogenic diet', 'intermittent fasting', 'holistic health', 'aromatherapy', 'acupuncture', 'homeopathy', 'naturopathy']
investment_options = ['stocks', 'bonds', 'real estate', 'cryptocurrency', 'mutual funds', 'ETFs', 'commodities', 'forex', 'startups', 'art', 'vintage cars', 'luxury watches', 'antiques', 'collectibles', 'private equity']
trends = ['sustainable living', 'remote work', 'e-commerce', 'digital marketing', 'cybersecurity', '3D printing', 'augmented reality', 'virtual reality', 'electric vehicles', 'space exploration', 'smart cities', 'biometrics', 'genomics', 'blockchain', 'machine learning']
economic_impacts = ['technology', 'healthcare', 'education', 'finance', 'manufacturing', 'agriculture', 'retail', 'transportation', 'energy', 'tourism', 'construction', 'media', 'telecommunications', 'pharmaceuticals', 'real estate']
legal_aspects = ['copyright', 'patent', 'trademark', 'contract law', 'corporate law', 'employment law', 'environmental law', 'family law', 'criminal law', 'international law', 'tax law', 'real estate law', 'bankruptcy law', 'civil rights law', 'immigration law']
cooking_methods = ['grilling', 'baking', 'frying', 'steaming', 'roasting', 'poaching', 'simmering', 'braising', 'stewing', 'smoking', 'sautéing', 'microwaving', 'pressure cooking', 'slow cooking', 'sous vide']
cultural_significance = ['festivals', 'music', 'dance', 'literature', 'architecture', 'fashion', 'cuisine', 'religion', 'art', 'theatre', 'cinema', 'folklore', 'traditions', 'languages', 'crafts']
maintenance_topics = ['cars', 'computers', 'smartphones', 'machinery', 'buildings', 'roads', 'bridges', 'aircraft', 'ships', 'trains', 'gardens']
sports = ['soccer', 'basketball', 'football', 'tennis', 'cricket', 'baseball', 'golf', 'rugby', 'hockey', 'volleyball', 'swimming', 'athletics', 'cycling', 'boxing', 'skiing']

# Placeholder

# Generating the data
query_list = []
field_list = []

for _ in range(100):
    for q in queries:
        if 'capital' in q:
            query_list.append(q.format(np.random.choice(countries)))
            field_list.append('Geography')
        elif 'work' in q:
            query_list.append(q.format(np.random.choice(technologies)))
            field_list.append('Science')
        elif 'stock price' in q:
            query_list.append(q.format(np.random.choice(companies)))
            field_list.append('Finance')
        elif 'programming' in q:
            query_list.append(q.format(np.random.choice(programming_languages)))
            field_list.append('Computer Science')
        elif 'data science' in q:
            query_list.append(q.format(np.random.choice(data_science_terms)))
            field_list.append('Data Science')
        elif 'history' in q:
            query_list.append(q.format(np.random.choice(histories)))
            field_list.append('History')
        elif 'health benefits' in q:
            query_list.append(q.format(np.random.choice(health_topics)))
            field_list.append('Health')
        elif 'invest' in q:
            query_list.append(q.format(np.random.choice(investment_options)))
            field_list.append('Finance')
        elif 'trends' in q:
            query_list.append(q.format(np.random.choice(trends)))
            field_list.append('Trends')
        elif 'affecting' in q:
            query_list.append(q.format(np.random.choice(economic_impacts)))
            field_list.append('Economy')
        elif 'rules' in q:
            query_list.append(q.format(np.random.choice(sports)))
            field_list.append('Sports')
        elif 'championship' in q:
            query_list.append(q.format(np.random.choice(sports)))
            field_list.append('Sports')
        elif 'techniques' in q:
            query_list.append(q.format(np.random.choice(sports)))
            field_list.append('Sports')
        elif 'train' in q:
            query_list.append(q.format(np.random.choice(sports)))
            field_list.append('Sports')
        elif 'practice' in q:
            query_list.append(q.format(np.random.choice(sports)))
            field_list.append('Sports')
        elif 'athletes' in q:
            query_list.append(q.format(np.random.choice(sports)))
            field_list.append('Sports')
        elif 'strategies' in q:
            query_list.append(q.format(np.random.choice(sports)))
            field_list.append('Sports')
        elif 'events' in q:
            query_list.append(q.format(np.random.choice(sports)))
            field_list.append('Sports')
        elif 'technology' in q:
            query_list.append(q.format(np.random.choice(sports)))
            field_list.append('Sports')
        elif 'equipment' in q:
            query_list.append(q.format(np.random.choice(sports)))
            field_list.append('Sports')

# Creating DataFrame
df = pd.DataFrame({'Query': query_list, 'Field': field_list})

# Saving to an Excel file
df.to_excel('queries_dataset.xlsx', index=False)
print('Excel file with example queries with sports-related categories has been created.')
