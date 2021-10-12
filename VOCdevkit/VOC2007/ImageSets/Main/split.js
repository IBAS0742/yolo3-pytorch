/**
 * 裁剪样本，用于测试代码时使用
 */
const fs = require('fs');

let files = ['test.txt','train.txt','trainval.txt','val.txt'];

let splitLen = 1000;

files.forEach(f => {
    console.log(`file = ${f}`);
    let content = fs.readFileSync(`./${f}`,'utf-8').split('\r\n')
        .filter(_ => {
            if (!fs.existsSync(`./../../Annotations/${_}.xml`)) {
                return false;
            }
            if (!fs.existsSync(`./../../JPEGImages/${_}.jpg`)) {
                return false;
            }

            return +_ < splitLen;
        });
    if (!content.length) {
        console.log(`file = [${files}] is zeros`);
    }
    fs.writeFileSync(`./${f}`,content.join('\r\n'),'utf-8');
});
