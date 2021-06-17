print("# We can have as many except clauses after the try, but that's a waste of time")
print("# Instead condense the excepts into one except (erro1, error2, ...):")

print("""
try:
    x = int("one")
    print("Print this " + x + "!")
except (ValueError, TypeError):
    print("ValueError exception raised, remove the try-except to see for yourself!") # output below
""")
try:
    x = int("one")
    print("Print this " + x + "!")
except (ValueError, TypeError):
    print("ValueError exception raised, remove the try-except to see for yourself!") # output below

print("\n# Now let's see the other exception catched!")

print("""
try:
    x = int("1")
    print("Print this " + x + "!")
except (ValueError, TypeError):
    print("TypeError exception raised, remove the try-except to see for yourself!") # output below
""")

try:
    x = int("1")
    print("Print this " + x + "!")
except (ValueError, TypeError):
    print("TypeError exception raised, remove the try-except to see for yourself!") # output below

print("\n# An error raised can be excepted by targeting it's own error or an inherited error")
print("# It all depends on which exception catches either of the errors first")

print("""
class GranDaddyError(Exception):
    print("GranDaddyError raised!")

class DaddyError(GranDaddyError):
    print("DaddyError raised!")

class SoyBoyError(DaddyError):
    print("SoyBoyError raised!")

for classs in [GranDaddyError, DaddyError, SoyBoyError]:
    try:
        raise classs()
    except DaddyError:
        print("Blame Daddy, he shouldn't have looked up to GranDaddy!")
    except SoyBoyError: 
        print("PC culture fucked SoyBoy up even more!")
    except GranDaddyError:
        print("Blame GranDaddy, he should've held Daddy accountable!") # output below
""")

class GranDaddyError(Exception):
    pass

class DaddyError(GranDaddyError):
    pass

class SoyBoyError(DaddyError):
    pass

for classs in [GranDaddyError, DaddyError, SoyBoyError]:
    try:
        raise classs()
    except DaddyError:
        print("Blame Daddy, he shouldn't have looked up to GranDaddy!")
    except SoyBoyError: 
        print("PC culture fucked SoyBoy up even more!")
    except GranDaddyError:
        print("Blame GranDaddy, he should've held Daddy accountable!") # output below

print("# The last except clause's exception name may be omitted but it will serve as a wildcard")
print("# Meaning that if any of the subsequent errors aren't excepted, this wildcard excepts it")

print("""
class CuntedOutError(Exception):
    pass

try:
    raise CuntedOutError()
except DaddyError:
    print("Daddy couldn't make you into a real man!")
except:
    print("Where the hell is your pair of huevos!") # output below
""")

class CuntedOutError(Exception):
    pass

try:
    raise CuntedOutError()
except DaddyError:
    print("Daddy couldn't make you into a real man!")
except:
    print("Where the hell is your pair of huevos!")

print("\n# You can have your try-except clauses do something else if an exception isn't raised")
print("# Have an else clause to execute something if an error isn't raised")

print("""
try:
    print("No error")
except DaddyError:
    print("Daddy couldn't make you into a real man!")
else:
    print("You are alright!") # output below
""")

try:
    print("No error")
except DaddyError:
    print("Daddy couldn't make you into a real man!")
else:
    print("You are alright!") # outputs below

