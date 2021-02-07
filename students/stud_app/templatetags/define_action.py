from django import template
register = template.Library()


@register.simple_tag
def update_variable(value):
	data = value
	return data
	
@register.filter
def to_str(value):
    return str(value)
	
	
class GlobalVariable(object):
	def __init__(self, varname, varval):
		self.varname = varname
		self.varval = varval

	def name(self):
		return self.varname

	def value(self):
		return self.varval

	def set(self, newval):
		self.varval = newval


class GlobalVariableSetNode(template.Node):
	def __init__(self, varname, varval):
		self.varname = varname
		self.varval = varval

	def render(self, context):
		gv = context.get(self.varname, None)
		if gv:
			gv.set(self.varval)
		else:
			gv = context[self.varname] = GlobalVariable(
				self.varname, self.varval)
		return ''


def setglobal(parser, token):
	try:
		tag_name, varname, varval = token.contents.split(None, 2)
	except ValueError:
		raise template.TemplateSyntaxError(
			"%r tag requires 2 arguments" % token.contents.split()[0])
	return GlobalVariableSetNode(varname, varval)


register.tag('setglobal', setglobal)


class GlobalVariableIncrementNode(template.Node):
	
	def __init__(self, varname):
		self.varname = varname

	def render(self, context):
		gv = context.get(self.varname, None)
		if gv is None:
			return ''
		gv.set(str(int(gv.value()) + 1))
		return ''


def incrementglobal(parser, token):
	try:
		tag_name, varname = token.contents.split(None, 1)
	except ValueError:
		raise template.TemplateSyntaxError(
			"%r tag requires arguments" % token.contents.split()[0])
	return GlobalVariableIncrementNode(varname)


register.tag('incrementglobal', incrementglobal)

class GlobalVariableDecrementNode(template.Node):
	def __init__(self, varname):
		self.varname = varname

	def render(self, context):
		gv = context.get(self.varname, None)
		if gv is None:
			return ''
		gv.set(str(int(gv.value()) - 1))
		return ''


def decrementglobal(parser, token):
	try:
		tag_name, varname = token.contents.split(None, 1)
	except ValueError:
		raise template.TemplateSyntaxError(
			"%r tag requires arguments" % token.contents.split()[0])
	return GlobalVariableIncrementNode(varname)


register.tag('decrementglobal', decrementglobal)


class GlobalVariableCopyNode(template.Node):
	def __init__(self, varname, varval):
		self.varname = varname
		self.varval = varval

	def render(self, context):
		gv = context.get(self.varname, None)
		gval = context[self.varval].value()
		if gv:
			gv.set(gval)
		else:
			gv = context[self.varname] = GlobalVariable(
				self.varname, gval)
		return ''


def Cpyglobal(parser, token):
	
	try:
		tag_name, varname, varval = token.contents.split(None, 2)
	except ValueError:
		raise template.TemplateSyntaxError(
			"%r tag requires 2 arguments" % token.contents.split()[0])
	return GlobalVariableCopyNode(varname, varval)


register.tag('Cpyglobal', Cpyglobal)


class GlobalVariableGetNode(template.Node):
	def __init__(self, varname):
		self.varname = varname

	def render(self, context):
		try:
			return context[self.varname].value()
		except AttributeError:
			return ''


def getglobal(parser, token):
	try:
		tag_name, varname = token.contents.split(None, 1)
	except ValueError:
		raise template.TemplateSyntaxError(
			"%r tag requires arguments" % token.contents.split()[0])
	return GlobalVariableGetNode(varname)


register.tag('getglobal', getglobal)
