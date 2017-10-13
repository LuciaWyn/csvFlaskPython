from flask import Flask, render_template, request
from flask import jsonify
import pandas as pd
from IPython.display import HTML

app = Flask(__name__)


@app.route('/')
def index():
    #return "hello"
    df = pd.read_csv('MobilePhoneMasts.csv')
    df = df.dropna(how='all')
    #df = df.groupby(by=['Name'])['Address1'].sum().to_frame()
   # df=df = df.drop(['Unnamed: 11'],axis=1)
    #df = df['Name']
    #df= "<<p>>dfd<</p>>"
    name = df['Name']
    ad1 = df['Address1']
    dfh = df.to_json(orient='records')
    l = len(df.index)
    ll = l-1
    #dfh = df.to_html()
    #df = df.values
    #dfh = df.to_json()
    #return render_template('index.html', lock=dfh)
    #return render_template('index.html', tables=df)
    return render_template('index1.html', jd=dfh, ct=ll, p="Home")
    #return dfn

@app.route('/rent')
def rent():
    df = pd.read_csv('MobilePhoneMasts.csv')
    df = df.dropna(how='all')
    dfl = df['Rent'].sum();
    dfl = "£"+str(dfl)
    #return df.to_html()
    return render_template('index2.html', t=dfl, p="Total Rent")

@app.route('/lease')
def lease():
    df = pd.read_csv('MobilePhoneMasts.csv')
    df = df.dropna(how='all')
    #df = df.drop(['Unnamed: 11'],axis=1)
    df= df.sort_values('Rent', axis=0, ascending=False)
    #return df.to_html()
    l = len(df.index)
    ll = l-1
    dfh = df.to_json(orient='records')
    return render_template('index1.html', jd=dfh, ct=ll, p="Leases in Ascending Order")

@app.route('/top5')
def top5():
    df = pd.read_csv('MobilePhoneMasts.csv')
    df = df.dropna(how='all')
    #df = df.drop(['Unnamed: 11'],axis=1)
    df = df.head()
    #df= df.sort_values('Rent', axis=0, ascending=False)
    #return df.to_html()
    l = len(df.index)
    ll = l-1
    dfh = df.to_json(orient='records')
    return render_template('index3.html', jd=dfh, ct = ll, p="Top 5 results")



@app.route('/top5/asc')
def top5asc():
    df = pd.read_csv('MobilePhoneMasts.csv')
    df = df.dropna(how='all')
    #df = df.drop(['Unnamed: 11'],axis=1)
    df = df.head()
    df= df.sort_values('Rent', axis=0, ascending=False)
    #return df.to_html()
    l = len(df.index)
    ll = l-1
    dfh = df.to_json(orient='records')
    return render_template('index3.html', jd=dfh, ct = ll, p="Top 5 results in Ascending order by Rent")

@app.route('/top5/dec')
def top5dec():
    df = pd.read_csv('MobilePhoneMasts.csv')
    df = df.dropna(how='all')
    df = df.head()
    df= df.sort_values('Rent', axis=0, ascending=True)
    l = len(df.index)
    ll = l-1
    dfh = df.to_json(orient='records')
    return render_template('index3.html', jd=dfh, ct = ll, p="Top 5 results in Ascending order by Rent")


@app.route('/tenants')
def tenants():
    #l = "<p>Tenants List</p>"
    #l = l+"<a href=""/tenants/ASL"">Arqiva Services ltd</a>"    
    return render_template('tennants1.html')

@app.route('/tenants/ASL')
def asl():
    df = pd.read_csv('MobilePhoneMasts.csv')
    df = df.dropna(how='all')
    df = df.loc[df['Tenant'] == 'Arqiva Services ltd']
    l = len(df.index)
    ll = l-1
    dfh = df.to_json(orient='records')
    return render_template('tennants.html', jd=dfh, ct=ll, cct=l, p="Arqiva Services ltd")


@app.route('/tenants/Vodafone')
def vl():
    df = pd.read_csv('MobilePhoneMasts.csv')
    df = df.dropna(how='all')
    df = df.loc[df['Tenant'] == 'Vodafone Ltd']
    l = len(df.index)
    ll = l-1
    dfh = df.to_json(orient='records')
    return render_template('tennants.html', jd=dfh, ct=ll, cct=l, p="Vodafone Ltd")


@app.route('/tenants/O2')
def ol():
    df = pd.read_csv('MobilePhoneMasts.csv')
    df = df.dropna(how='all')
    df = df.loc[df['Tenant'] == 'O2 (UK) Ltd']
    l = len(df.index)
    ll = l-1
    dfh = df.to_json(orient='records')
    return render_template('tennants.html', jd=dfh, ct=ll, cct=l, p="O2 (UK) Ltd")


@app.route('/tenants/EEL')
def eel():
    df = pd.read_csv('MobilePhoneMasts.csv')
    df = df.dropna(how='all')
    df = df[df['Tenant'].str.contains('Everything Everywhere Ltd')]
    l = len(df.index)
    ll = l-1
    dfh = df.to_json(orient='records')
    return render_template('tennants.html', jd=dfh, ct=ll, cct=l, p="Everything Everywhere Ltd")


@app.route('/tenants/Hutchinson')
def hutch():
    df = pd.read_csv('MobilePhoneMasts.csv')
    df = df.dropna(how='all')
    df = df[df['Tenant'].str.contains('Hutchinson')]
    l = len(df.index)
    ll = l-1
    dfh = df.to_json(orient='records')
    return render_template('tennants.html', jd=dfh, ct=ll, cct=l, p="Hutchinson")


@app.route('/tenants/CTI')
def cti():
    df = pd.read_csv('MobilePhoneMasts.csv')
    df = df.dropna(how='all')
    df = df.loc[df['Tenant'] == 'Cornerstone Telecommunications Infrastructure']
    l = len(df.index)
    ll = l-1
    dfh = df.to_json(orient='records')
    return render_template('tennants.html', jd=dfh, ct=ll, cct=l, p="Cornerstone Telecommunications Infrastructure")


@app.route('/times')
def times():
    df1 = pd.read_csv('MobilePhoneMasts.csv')
    df1 = df1.dropna(how='all')
    #df1['Start'] = df1['LeaseStart'].dt.strftime('%d/%m/%Y')
    df1['Start'] = pd.to_datetime(df1.LeaseStart)
    df1['End'] = pd.to_datetime(df1.LeaseEnd)
    ts = pd.to_datetime('31/05/1999')
    td = pd.to_datetime('31/08/2007')
    #df1['Start'] = pd.to_datetime(df1['Start'])
    df2 = df1.loc[(df1.Start >= ts) & (df1.Start <= td)]
    df2['Start'] = df2['Start'].dt.strftime('%d/%m/%Y')
    df2['End'] = df2['End'].dt.strftime('%d/%m/%Y')
    df2 = df2.drop(['LeaseStart'],axis=1)
    df2 = df2.drop(['LeaseEnd'],axis=1)
    l = len(df2.index)
    ll = l-1
    dfh = df2.to_json(orient='records')
    return render_template('index1.html', jd=dfh, ct=ll, p="From 1/06/99 to 31/08/07")

@app.route('/add')
def add():
    return render_template('form.html')

@app.route('/added', methods=['POST'])
def added():
    name = request.form['name']
    ad1 = request.form['adr1']
    ad2 = request.form['adr2']
    ad3 = request.form['adr3']
    ad4 = request.form['adr4']
    sdd = request.form['sd']
    u = request.form['unit']
    t = request.form['tenant']
    y = request.form['year']
    r = request.form['rent']
    r = str(r)
    ssdd = str(sdd)

    if(ad1 is None):
        ad1 = ''
    if(ad2 is None):
        ad2 = ''
    if(ad3 is None):
        ad3 = ''
    if(ad4 is None):
        ad4 = ''
    if (len(sdd)==1):
            ssdd="0"+ssdd

    sdy = request.form['sy']
    ssdy = str(sdy)
    if(len(ssdy)!=2):
        ssdy = (ssdy[-2:])
        
    sdate = ssdd+"-"+request.form['sm']+"-"+ssdy

    edd = request.form['ed']
    eedd = str(edd)
    if (len(eedd)==1):
            eedd="0"+eedd

    edy = request.form['ey']
    eedy = str(edy)
    if(len(eedy)!=2):
        eedy = (eedy[-2:])
    
    edate = eedd+"-"+request.form['em']+"-"+eedy
    import csv
    with open('MobilePhoneMasts.csv', 'a') as newFile:
        newFileWriter = csv.writer(newFile)
        newFileWriter.writerow([name, ad1, ad2, ad3,ad4, u, t, sdate, edate, y, r])
    
    return render_template('index2.html', t="<p>Data sucessfully added</p>", p="Added")

if __name__ == '__main__':
    app.run()
