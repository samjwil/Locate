from flask import render_template, request, jsonify
from flaskexample import app
import Model_Plot


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

#call from button on master
@app.route('/go')
def go():

    input_ = request.args.get('query', '')
    everythingOK=True

    output=Model_Plot.main(input_)
    # print('output:', output)
    time = output['time']
    out1 = ','.join(output['out1'])
    out2 = ','.join(output['out2'])
    out3 = ','.join(output['out3'])
    lat = ','.join(output['lat'])
    lng = ','.join(output['lng'])
    mcol = output['mcol']
    result_dict = output['result_dict']
    geoname=output['geoname']
    mvals=output['mvals']
    time2=output['time2']
    names=output['names']
    links=output['links']
    return render_template(
        'go.html',
        query = output,
        time = time,
        lat = lat,
        lng = lng,
        out1 = out1,
        out2 = out2,
        out3 = out3,
        city = geoname,
        result_dict = result_dict,
        mcol = mcol,
        time2 = time2,
        mvals = mvals,
        links = links,
        names = names
    )
