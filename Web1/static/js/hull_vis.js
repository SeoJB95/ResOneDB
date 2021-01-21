import './three.module.js'
import {NURBSCurve} from './NURBSCurve.js'
var onelineDrawing = function(oneline,material){
      let controlPoints  =  [];
      oneline.control.forEach(function(line){
      controlPoints.push(new THREE.Vector3(line[0],line[1],line[2]))
      })
      var knots =oneline.U;

      var curve = new NURBSCurve( 3, knots, controlPoints, 0, 0 );
      var vertices = curve.getPoints( controlPoints.length * 7 );
      var positions = new Float32Array( vertices.length * 3 );
      vertices.forEach( function ( vertex, i ) {
        vertex.toArray( positions, i * 3 );
      });
      var geometry = new THREE.BufferGeometry();
      geometry.setAttribute( 'position', new THREE.BufferAttribute( positions, 3 ) );
      var line_gl = new THREE.Line(geometry,material);
      return line_gl
}
var partDrawing = function(LinesDictionary,material){
      var lineList = [];
      for (var key in LinesDictionary){
        lineList.push(onelineDrawing(LinesDictionary[key],material));
      }
      return lineList
}
var importHull = function(inputjson,scene,material){
  //TEST!!
  //{% autoescape off %}
  //var hull = JSON.parse('{{testjson}}')
  var hull = JSON.parse(inputjson)
  //{% endautoescape %}
  //const material = new THREE.LineBasicMaterial( { color: 0x0000ff } );
  var FWLs = partDrawing(hull.Waterline.Fore,material);
  FWLs.forEach(function(wl){scene.add(wl);})
  var AWLs = partDrawing(hull.Waterline.After,material);
  AWLs.forEach(function(wl){scene.add(wl);})
  var Fsts = partDrawing(hull.Station.After,material);
  Fsts.forEach(function(wl){scene.add(wl);})
  var Asts = partDrawing(hull.Station.Fore,material);
  Asts.forEach(function(wl){scene.add(wl);})
  scene.add(onelineDrawing(hull.STEM,material));
  scene.add(onelineDrawing(hull.STERN,material));
  scene.add(onelineDrawing(hull.STERN,material));
  scene.add(onelineDrawing(hull.FOBA,material));
  scene.add(onelineDrawing(hull.FOBF,material));
  scene.add(onelineDrawing(hull.FOSA,material));
  scene.add(onelineDrawing(hull.FOSF,material));
  scene.add(onelineDrawing(hull.Boss,material));


  var special = [hull.STEM,hull.STERN,hull.FOBA,hull.FOBF,hull.FOSA,hull.FOSF]

//import Hull end
}
export {importHull}
