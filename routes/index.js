var express = require('express');
var router = express.Router();
const { spawn } = require('child_process');


/* GET home page. */
router.get('/', function (req, res, next) {
  

  res.render('index', { title: 'Express' });
});

router.post('/search',(req,res)=>{
  console.log(req.body['policy']);
  const pyProg = spawn('python', ['public/scripts/script.py',req.body['policy']]);
  p = ""
  ne = ""
  nu = ""
  pyProg.stdout.on('data', function (data) {

    ne = (data.toString()[0]+data.toString()[1])
  
    nu = (data.toString()[4]+data.toString()[5])
    p = (data.toString()[8]+data.toString()[9])

    console.log(ne+nu+p);
  ne = Number(ne)
  nu = Number(nu)
  p = Number(p)
  res.render('index', { title: 'Express',pos:p,neg:ne,neu:nu});

  });
  
})

module.exports = router;
