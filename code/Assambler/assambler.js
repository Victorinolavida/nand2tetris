//const FOLDER_FILES = "/Users/victorino.ruiz/Desktop/nand2tetris/projects/06/";
const fs = require("fs");
//const { translate } = require("./code");

const args = process.argv.slice(2);

/*
function main() {
  let FILE_PATH = "";

  if (args.length === 0) throw new Error("nombre del archivo vacio");

  const folders = [];
  fs.readdirSync(FOLDER_FILES).forEach((file) => {
    if (file.toString() !== "Assambler" && file.toString()!==".DS_Store") {
      folders.push(FOLDER_FILES + file + "/");
    }
  });

  if (folders.length === 0) throw new Error("la carpeta 06 esta vacia");

  while (folders.length !== 0) {
    const folder = folders.shift();
    fs.readdirSync(folder).forEach((file) => {
      if (args[0] == file) {
        FILE_PATH = folder + `${args[0]}`;
      }
    });
  }
  console.log(FILE_PATH);
  if (!FILE_PATH) throw new Error(`No se encontro el archivo ${args[0]}`);

  const data = fs.readFileSync(FILE_PATH, "utf8").split("\n").filter(Boolean);

  const code_machine = translate(data);

  //writing file
  
  fs.writeFileSync(`${args[0].replace('asm','hack')}`,code_machine.join("\n"));
  console.log(`file ${args[0].replace('asm','hack')} saved`)
}

try {
  main();
  
} catch (e) {
  console.error("Error: ", e.message);
}
*/

const {Parcer} = require("./code")


class Main{
  constructor(file){
    this.file_name = file
    this.error  = undefined;
    // this._file = this.open_file(file)
    //this.write_code()
  }

  open_file(){
    try {

      let file = fs.readFileSync(this.file_name, "utf8").split("\n").filter(Boolean);
      this._file = file;
    } catch (error) {
      console.error(`Error: file ${this.file_name} does not found`)
      this.error = true;
    }
  }


  write_code(){
    this.open_file()

    if(this.error || !this._file){
      console.log(`Error: ${this.file_name} does not exist`)
    };

    const code_parcered = new Parcer(this._file).code_asm
    // console.log(code_parcered)
    fs.writeFileSync(`${this.file_name.replace('asm','hack')}`,code_parcered.join("\n"));
    console.log(`---------  ${this.file_name.replace('asm','hack')} has been created  -------`)
  }


}


const file = new Main(args[0])
file.write_code()

