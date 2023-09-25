const { spawn } = require('child_process');

module.exports = {
    getdata: (data) => {
        return new Promise(async (resolve, reject) => {
            const pyProg = spawn('python', ['public/scripts/script.py', req.body['policy']]);
            p = ""
            ne = ""
            nu = ""
            await pyProg.stdout.on('data', function (data) {
                if(data==null){
                    
                }

                ne = (data.toString()[0] + data.toString()[1]);

                nu = (data.toString()[4] + data.toString()[5]);
                p = (data.toString()[8] + data.toString()[9]);

                console.log(ne + nu + p);
                ne = Number(ne);
                nu = Number(nu);
                p = Number(p);

            });
        });
    }
};