import python

/**
 * @name Avoid os.system
 * @description Flags every call to os.system as unsafe
 */
class OsSystemCall extends Call {
  OsSystemCall() { 
    this.getTarget().getName() = "system" and
    this.getTarget().getDeclaringType().hasQualifiedName("os") 
  }
}

from OsSystemCall call
select call, "Avoid using os.system; prefer subprocess or other safe APIs."
