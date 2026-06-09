from pydantic import BaseModel, Field
from typing import Optional, Any, Union, Literal, List


class BaseElement(BaseModel):
    id: str
    elementType: str


# Personal Info Field

class PersonalFieldProps(BaseModel):
    label: str
    required: bool = False
    hidden: bool = False
    width: int = 100

class FullNameProps(PersonalFieldProps):
    placeholder: str
    shortLabel: str
    queryKey: str
    minLength: int = 0
    maxLength: int = 100
    autocomplete: str = ""

class FullNameElement(BaseElement):
    elementType: Literal["full-name"]
    props: FullNameProps

class FirstNameElement(BaseElement):
    elementType: Literal["first-name"]
    props: FullNameProps

class LastNameElement(BaseElement):
    elementType: Literal["last-name"]
    props: FullNameProps

class PhoneProps(PersonalFieldProps):
    placeholder: str
    shortLabel: str
    queryKey: str
    enableCountryPicker: bool = True
    countryCode: str = "+1"
    validatePhone: bool = False

class PhoneElement(BaseElement):
    elementType: Literal["phone"]
    props: PhoneProps

class EmailProps(PersonalFieldProps):
    placeholder: str
    shortLabel: str
    queryKey: str
    validateEmail: bool = False

class EmailElement(BaseElement):
    elementType: Literal["email"]
    props: EmailProps

class DatePickerProps(PersonalFieldProps):
    placeholder: str
    shortLabel: str
    queryKey: str
    dateFormat: str
    dateSeparator: str = "-"
    disablePicker: bool = False

class DatePickerElement(BaseElement):
    elementType: Literal["date-picker"]
    props: DatePickerProps


# Text Field

class TextFieldProps(BaseModel):
    label: str
    required: bool = False
    shortLabel: str = ""
    queryKey: str
    width: int = 100
    customFieldName: str = ""
    uniqueKey: str = ""

class SingleLineProps(TextFieldProps):
    hidden: bool = False
    placeholder: str

class SingleLineElement(BaseElement):
    elementType: Literal["single-line"]
    props: SingleLineProps

class MultiLineProps(TextFieldProps):
    hidden: bool = False
    placeholder: str
    rows: int = 4

class MultiLineElement(BaseElement):
    elementType: Literal["multi-line"]
    props: MultiLineProps

class TextBoxRow(BaseModel):
    id: str
    label: str
    value : str

class TextBoxListProps(TextFieldProps):
    textBoxRows : List[TextBoxRow]

class TextBoxListElement(BaseElement):
    elementType : Literal["text-box-list"]
    props: TextBoxListProps


#Customized

class TncBlock(BaseModel):
    id: str
    content: str = "<p>I agree to terms &amp; conditions provided by the company. By providing my phone number, I agree to receive text messages from the business.</p>"

class TcProps(BaseModel):
    label: str
    required : bool = False
    queryKey : str
    textColor : str
    linkColor : str
    tncBlocks : List[TncBlock]

class TcElement(BaseElement):
    elementType: Literal["t-c"]
    props: TcProps

class ScoreProps(BaseModel):
    label: str
    placeholder : str
    required : bool = False

class ScoreElement(BaseElement):
    elementType: Literal["score"]
    props : ScoreProps

class Padding(BaseModel):
    top : int
    right : int
    bottom: int
    left : int

class Shadow(BaseModel):
    color: str
    horizontal: int
    vertical : int
    blur : int
    spread : int

class TextBlockProps(BaseModel):
    label : str
    content: str
    backgroundColor: str
    fontColor : str
    fontFamily: str
    fontSize : int
    fontWeight: int
    border : int
    borderColor : str
    borderType: str
    cornerRadius : int
    padding: Padding
    shadow : Shadow

class TextBlock(BaseElement):
    elementType : Literal["text-block"]
    props : TextBlockProps


#Other ELements

class ImageProps(BaseModel):
    label : str
    src : str
    alt : str
    spanFullWidth : bool = True
    widthPx : int
    heightPx : Optional[int] = None
    alignment : str

class ImageElement(BaseElement):
    elementType : Literal["image"]
    props : ImageProps
    
class FileUploadProps(BaseModel):
    label : str
    required : bool = False
    multiple: bool = False
    maxSize: int = 10
    allowedTypes: str = "pdf, png, docx"
    spanFullWidth : bool = True

class FileUploadElement(BaseElement):
    elementType: Literal["file-upload"]
    props: FileUploadProps


# Address Fields

class CityProps(PersonalFieldProps):
    placeholder: str
    shortLabel: str
    queryKey: str
    minLength: int = 0
    maxLength: int = 100

class CityElement(BaseElement):
    elementType: Literal["city"]
    props: CityProps

class StateProps(PersonalFieldProps):
    placeholder: str
    shortLabel: str = ""
    queryKey: str = ""

class StateElement(BaseElement):
    elementType: Literal["state"]
    props: StateProps

class CountryProps(PersonalFieldProps):
    placeholder: str
    shortLabel: str = ""
    queryKey: str = ""

class CountryElement(BaseElement):
    elementType: Literal["country"]
    props: CountryProps

class PostalCodeProps(PersonalFieldProps):
    placeholder: str
    shortLabel: str = ""
    queryKey: str = ""

class PostalCodeElement(BaseElement):
    elementType: Literal["postal-code"]
    props: PostalCodeProps

class OrganizationProps(PersonalFieldProps):
    placeholder: str
    shortLabel: str
    queryKey: str
    minLength: int = 0
    maxLength: int = 100

class OrganizationElement(BaseElement):
    elementType: Literal["organization"]
    props: OrganizationProps

class WebsiteProps(PersonalFieldProps):
    placeholder: str
    shortLabel: str
    queryKey: str
    validateUrl: bool = False

class WebsiteElement(BaseElement):
    elementType: Literal["website"]
    props: WebsiteProps


# Number Fields

class NumberProps(TextFieldProps):
    hidden: bool = False
    placeholder: str
    minValue: int = 0
    maxValue: int = 999999

class NumberElement(BaseElement):
    elementType: Literal["number"]
    props: NumberProps

class MonetaryProps(PersonalFieldProps):
    placeholder: str
    shortLabel: str
    queryKey: str
    currency: str = "$"
    currencyPosition: str = "before"
    alignment: str = "left"
    minValue: int = 0
    maxValue: int = 999999

class MonetaryElement(BaseElement):
    elementType: Literal["monetary"]
    props: MonetaryProps


# Selection Fields

class SelectOption(BaseModel):
    id: str
    label: str
    value: str

class SelectProps(TextFieldProps):
    hidden: bool = False
    placeholder: str = ""
    selectOptions: List[SelectOption]
    selected: str = ""

class SelectElement(BaseElement):
    elementType: Literal["select"]
    props: SelectProps

class CheckboxOption(BaseModel):
    id: str
    label: str
    checked: bool = False

class CheckboxProps(TextFieldProps):
    hidden: bool = False
    placeholder: str = ""
    options: List[CheckboxOption]

class CheckboxElement(BaseElement):
    elementType: Literal["checkbox"]
    props: CheckboxProps

class RadioOption(BaseModel):
    id: str
    label: str
    checked: bool = False

class RadioProps(TextFieldProps):
    hidden: bool = False
    placeholder: str = ""
    radioOptions: List[RadioOption]

class RadioElement(BaseElement):
    elementType: Literal["radio"]
    props: RadioProps


# Rating Field

class RatingProps(BaseModel):
    label: str
    required: bool = False
    shortLabel: str = ""
    width: int = 100
    ratingIcon: str = "star"
    ratingAlign: str = "center"
    ratingCount: int = 5
    ratingMinLabel: str = ""
    ratingMaxLabel: str = ""
    ratingStoreMode: str = "absolute"
    ratingColorSelected: str = "#facc15"
    ratingColorUnselected: str = "#e5e7eb"
    customFieldName: str = ""
    uniqueKey: str = ""

class RatingElement(BaseElement):
    elementType: Literal["rating"]
    props: RatingProps


# Button Field

class ButtonProps(BaseModel):
    label: str
    fullWidth: bool = False
    align: str = "center"
    subText: str = ""
    customWidth: str = ""
    fontFamily: str = "System UI"
    fontSize: int = 14
    fontWeight: int = 600
    textColor: str = "#ffffff"
    bgColor: str = "#3b82f6"
    borderWidth: int = 0
    borderStyle: str = "solid"
    borderColor: str = "#3b82f6"
    borderRadius: int = 8
    padTop: int = 12
    padRight: int = 24
    padBottom: int = 12
    padLeft: int = 24
    shadowX: int = 0
    shadowY: int = 2
    shadowBlur: int = 4
    shadowSpread: int = 0
    shadowColor: str = "rgba(0,0,0,0.1)"

class ButtonElement(BaseElement):
    elementType: Literal["button"]
    props: ButtonProps

# class MonetaryProps(BaseModel):
#     label: str
#     required : bool = False
#     placeholder : str
#     shortLabel : str
#     queryKey : str
#     width : int
#     currency : str = "$"
#     currencyPosition : str
#     alignment : str

# class MonetaryElement(BaseElement):
#     elementType : Literal["monetary"]
#     props : MonetaryProps


CanvasElement = Union[
    FullNameElement,
    FirstNameElement,
    LastNameElement,
    EmailElement,
    PhoneElement,
    DatePickerElement,
    CityElement,
    StateElement,
    CountryElement,
    PostalCodeElement,
    OrganizationElement,
    WebsiteElement,
    SingleLineElement,
    MultiLineElement,
    TextBoxListElement,
    SelectElement,
    CheckboxElement,
    RadioElement,
    NumberElement,
    MonetaryElement,
    RatingElement,
    TextBlock,
    ImageElement,
    FileUploadElement,
    TcElement,
    ScoreElement,
    ButtonElement,
]



class ImageSchema(BaseModel):
    file: Optional[Any] = None
    url: Optional[str] = None


class UiStateSchema(BaseModel):

    is_previewing: bool = Field(
        default=False,
        alias="isPreviewing"
    )

    canvas_view: str = Field(
        default="desktop",
        alias="canvasView"
    )

    canvas_columns: int = Field(
        default=1,
        alias="canvasColumns"
    )

    field_spacing: int = Field(
        default=16,
        alias="fieldSpacing"
    )

    label_alignment: str = Field(
        default="left",
        alias="labelAlignment"
    )

    show_label: bool = Field(
        default=True,
        alias="showLabel"
    )

    input_style: str = Field(
        default="box",
        alias="inputStyle"
    )

    form_width: int = Field(
        default=650,
        alias="formWidth"
    )

    label_width: int = Field(
        default=100,
        alias="labelWidth"
    )

    padding_top: int = Field(
        default=40,
        alias="paddingTop"
    )

    padding_right: int = Field(
        default=40,
        alias="paddingRight"
    )

    padding_bottom: int = Field(
        default=30,
        alias="paddingBottom"
    )

    padding_left: int = Field(
        default=40,
        alias="paddingLeft"
    )

    background_color: str = Field(
        default="#ffffff",
        alias="backgroundColor"
    )

    font_color: str = Field(
        default="#000000",
        alias="fontColor"
    )

    input_background_color: str = Field(
        default="#FFFFFF",
        alias="inputBackgroundColor"
    )

    background_image: ImageSchema = Field(
        default_factory=ImageSchema,
        alias="backgroundImage"
    )

    header_image: ImageSchema = Field(
        default_factory=ImageSchema,
        alias="headerImage"
    )

    border_width: int = Field(
        default=1,
        alias="borderWidth"
    )

    corner_radius: int = Field(
        default=4,
        alias="cornerRadius"
    )

    border_color: str = Field(
        default="#D3D3D3",
        alias="borderColor"
    )

    border_style: str = Field(
        default="solid",
        alias="borderStyle"
    )

    shadow_color: str = Field(
        default="#00000020",
        alias="shadowColor"
    )

    shadow_horizontal: int = Field(
        default=0,
        alias="shadowHorizontal"
    )

    shadow_vertical: int = Field(
        default=2,
        alias="shadowVertical"
    )

    shadow_blur: int = Field(
        default=8,
        alias="shadowBlur"
    )

    shadow_spread: int = Field(
        default=0,
        alias="shadowSpread"
    )

    input_font_color: str = Field(
        default="#000000",
        alias="inputFontColor"
    )

    active_tag_color: str = Field(
        default="#2563EB",
        alias="activeTagColor"
    )

    input_border_width: int = Field(
        default=1,
        alias="inputBorderWidth"
    )

    input_border_color: str = Field(
        default="#D3D3D3",
        alias="inputBorderColor"
    )

    input_corner_radius: int = Field(
        default=10,
        alias="inputCornerRadius"
    )

    input_width: str = Field(
        default="100%",
        alias="inputWidth"
    )

    input_border_style: str = Field(
        default="solid",
        alias="inputBorderStyle"
    )

    input_padding_top: int = Field(
        default=12,
        alias="inputPaddingTop"
    )

    input_padding_right: int = Field(
        default=12,
        alias="inputPaddingRight"
    )

    input_padding_bottom: int = Field(
        default=12,
        alias="inputPaddingBottom"
    )

    input_padding_left: int = Field(
        default=12,
        alias="inputPaddingLeft"
    )

    input_shadow_color: str = Field(
        default="#00000010",
        alias="inputShadowColor"
    )

    input_shadow_horizontal: int = Field(
        default=0,
        alias="inputShadowHorizontal"
    )

    input_shadow_vertical: int = Field(
        default=1,
        alias="inputShadowVertical"
    )

    input_shadow_blur: int = Field(
        default=4,
        alias="inputShadowBlur"
    )

    input_shadow_spread: int = Field(
        default=0,
        alias="inputShadowSpread"
    )

    label_color: str = Field(
        default="#000000",
        alias="labelColor"
    )

    label_font_family: str = Field(
        default="Open Sans",
        alias="labelFontFamily"
    )

    label_font_size: int = Field(
        default=14,
        alias="labelFontSize"
    )

    label_font_weight: int = Field(
        default=400,
        alias="labelFontWeight"
    )

    short_label_color: str = Field(
        default="#666666",
        alias="shortLabelColor"
    )

    short_label_font_family: str = Field(
        default="Open Sans",
        alias="shortLabelFontFamily"
    )

    short_label_font_size: int = Field(
        default=12,
        alias="shortLabelFontSize"
    )

    short_label_font_weight: int = Field(
        default=400,
        alias="shortLabelFontWeight"
    )

    placeholder_color: str = Field(
        default="#74797B",
        alias="placeholderColor"
    )

    placeholder_font_family: str = Field(
        default="Noto Sans JP",
        alias="placeholderFontFamily"
    )

    placeholder_font_size: int = Field(
        default=14,
        alias="placeholderFontSize"
    )

    placeholder_font_weight: int = Field(
        default=400,
        alias="placeholderFontWeight"
    )

    class Config:
        populate_by_name = True