var Vec2D = (function(){
  var create = function(x, y){
    var obj = Object.create(def);
    obj.setXY(x, y);

    return obj;
  };


  var def ={
    _x: 1,
    _y: 0,

    getX: function()
    {
      return this._x;
    },

    setX: function(value)
    {
      this._x = value;
    },

    getY: function()
    {
      return this._y;
    },

    setY: function(value)
    {
      this._y = value;
    },

    setXY: function(x, y)
    {
      this._x = x;
      this._y = y;
    },

    getLength: function()
    {
      return Math.sqrt(this._x * this._x + this._y * this._y);
    },

    setLength: function(length)
    {
      var angle = this.getAngle();
      this._x = Math.cos(angle) * length;
      this._y = Math.sin(angle) * length;
    },

    getAngle: function()
    {
      return Math.atan2(this._y, this._x);
    },

    setAngle: function(angle)
    {
      var length = this.getLength();
      this._x = Math.cos(angle) * length;
      this._y = Math.sin(angle) * length;
    },

    add: function(vector)
    {
      this._x += vector.getX();
      this._y += vector.getY();
    },

    sub: function(vector)
    {
      this._x -= vector.getX();
      this._y -= vector.getY();
    },

    mul: function(value)
    {
      this._x *= value;
      this._y *= value;
    },

    div: function(value)
    {
      this._x /= value;
      this._y /= value;
    }
  };

  return {create:create};
}());


function catStrat4(cx, cy, rx, ry, Lx, Ly, ratThrustX, ratThrustY, catMaxThrust, losAngOld,  losLenOld, init4, catVelX, catVelY, ratVelX, ratVelY){

      var angle = 0;
      var nsep = 0;
      const N = 1
      var losAngleOld;
      var losAngleNew;
      var losLengthOld;
      var losLengthNew;
      var ratThrust = Vec2D.create(0, 0);
      ratThrust.setXY(ratThrustX, ratThrustY);
      var ratDrag = Vec2D.create(0,0);
      ratDrag.setXY(ratVelX * 5, ratVelY * 5);
      var direction = Math.PI * 0.5
      var catThrust = Vec2D.create(0,0);

      var W = 3

      var x = -(cx-rx);                     /* cat relative to rat in x*/
      var y = -(cy-ry);                     /* cat relative to rat in y*/
      x = (x > Lx/2) ? (x-Lx) : ((x<-Lx/2) ? (x+Lx) : x);      /* find the shorest distance vector from rat to cat */
      y = (y>Ly/2) ? (y-Ly) : ((y<-Ly/2) ? (y+Ly) : y);      /* on torus. */
      nsep = Math.sqrt((Math.pow(x,2)+Math.pow(y,2)));            /* relative separation normalized to box size */
      angle = Math.atan2(y,x);

      if (init4 == 1) {
        losAngleOld = angle
        losAngleNew = losAngleOld;
        losLengthOld = nsep
        losLengthNew = losLengthOld+1;
      }else{
        losAngleOld = losAngOld;
        losAngleNew = angle
        losLengthOld = losLenOld;
        losLengthNew = nsep
      }

      var lineOfSight_rate = losAngleNew - losAngleOld;
      var closingVelocity =  losLengthOld - losLengthNew;

      var tgo = (losLengthNew/closingVelocity);
      var v_rel_x = -(catVelX - ratVelX);
      var v_rel_y = -(catVelY - ratVelY);
      var n_x = (W/(tgo^2))*(x + tgo*v_rel_x + (tgo^2/2)*(ratThrust.getX()-ratDrag.getX()));
      var n_y = (W/(tgo^2))*(y + tgo*v_rel_y + (tgo^2/2)*(ratThrust.getY()-ratDrag.getY()));

      catThrust.setXY(n_x + catVelX * 2, n_y + catVelY * 2);



      var los_thrust = Vec2D.create(0,0);
      los_thrust.setLength(catThrust.getLength())
      los_thrust.setAngle(losAngleNew);


      catThrust.add(los_thrust);

      catThrust.setLength(catMaxThrust)


      var thrustArray = [catThrust.getX(), catThrust.getY(), angle, nsep];
      return thrustArray;
};
