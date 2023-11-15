program GruposDeTrabalho;

const
  MAX_E = 999999;

var
  E, M, D, i, j, k, X, Y, U, V: integer;
  likePairs, dislikePairs: array[1..MAX_E] of set of integer;
  groups: array[1..MAX_E div 3] of array[1..3] of integer;
  violations: integer;

begin
  readln(E, M, D);

  for i := 1 to M do
  begin
    readln(X, Y);
    Include(likePairs[X], Y);
    Include(likePairs[Y], X);
  end;

  for i := 1 to D do
  begin
    readln(U, V);
    Include(dislikePairs[U], V);
    Include(dislikePairs[V], U);
  end;

  for i := 1 to E div 3 do
    readln(groups[i][1], groups[i][2], groups[i][3]);

  violations := 0;
  for i := 1 to E div 3 do
    for j := 1 to 2 do
      for k := j + 1 to 3 do
      begin
        if groups[i][j] in likePairs[groups[i][k]] then
          Inc(violations);
        if groups[i][j] in dislikePairs[groups[i][k]] then
          Inc(violations);
        if groups[i][k] in likePairs[groups[i][j]] then
          Inc(violations);
        if groups[i][k] in dislikePairs[groups[i][j]] then
          Inc(violations);
      end;

  writeln(violations);
end.